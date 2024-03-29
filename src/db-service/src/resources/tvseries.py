import json
import logging
import logging.config
import threading
import requests

import grpc

from flask import jsonify, request
from flask_restful import Resource, reqparse

from common import settings, utils
from db import Database

import imdb_pb2
import imdb_pb2_grpc


try:
    logging.config.fileConfig(utils.get_logger_cfg_fpath())
except FileNotFoundError as e:
    print(e)
logger = logging.getLogger(__name__)


def schedule_extraction_job(series_name: str):
    logger.info(("Attempting to schedule a extraction job "
                 f"for `{series_name}`"))
    r = requests.post(settings.JOB_SERVICE_API, params={
        'name': series_name
    })
    if r.status_code == 202:
        logger.info(f"Job scheduling for '{series_name}' successful")
    else:
        logger.error(f"Job scheduling for '{series_name}' not successful.")


class TVSeries(Resource):
    def __init__(self):
        self._parser = reqparse.RequestParser()
        self._parser.add_argument('name', type=str, required=True)

    def get(self):
        args = self._parser.parse_args()
        identifier = args['name']
        logger.info(f"Initiating GET `{identifier}`")

        with Database() as db:
            resp = db.find(identifier)

        if resp is None:
            logger.error(f"`{identifier}` could not be found in the database.")
            with grpc.insecure_channel('job-service:3777') as channel:
                logger.info(("Going to submit a job creation request "
                             f"for {identifier}"))
                job_service_stub = imdb_pb2_grpc.JobServiceStub(channel)
                resp = job_service_stub.CreateJob(
                    imdb_pb2.CreateJobRequest(target_name=identifier)
                )
                logger.info(f"Job creation response: {resp}")
            return {"message": f"TVSeries '{identifier}' not found"}, 404
        else:
            logger.info((f"{identifier} found in database; "
                         "Returning the series' data."))
            return jsonify(json.loads(resp.to_json()))

    def post(self):
        with Database() as db:
            resp, msgs = db.add_from_dict(request.json)

        if resp == False:
            return {'Messages': msgs}, 400
        return request.json

    def delete(self):
        args = self._parser.parse_args()
        identifier = args['name']

        with Database() as db:
            status = db.delete(identifier)

        if status == False:
            return {"message": f"TVSeries '{identifier}' not found"}, 404
        else:
            return {"message": f"Deleted '{identifier}'"}, 204

    def _start_bg_extracton_thread(self, series_name: str):
        """Schedule an extraction job in the background, if the series cannot 
        be found in the database.
        """
        t = threading.Thread(target=schedule_extraction_job,
                             args=(series_name,), daemon=True)
        t.start()
        if t.ident is None:
            logger.error(("Unable to start a background thread for ",
                          "extraction."))
        else:
            logger.info(("Start a background thread for extraction "
                         f"job scheduling, TID={t.ident}"))
