import logging
from logging.config import fileConfig
import os
import yaml

from common.utils import get_logger_cfg_fpath

CONFIG_FNAME = "cfg/base_cfg.yml"

try:
    fileConfig(get_logger_cfg_fpath())
except FileNotFoundError as e:
    print(e)
logger = logging.getLogger(__name__)


class ExtractorConfigFileNotFoundError(FileNotFoundError):
    """Raised when extractor config file is not found."""
    pass


class ExtractorConfig:
    """This class contains configurations specified in the config file.
    The default location for config file is `src/config.yml`.
    """

    def __init__(self, fname=CONFIG_FNAME):
        try:
            with open(os.path.abspath(fname), 'r') as cfgfile:
                cfg = yaml.safe_load(cfgfile)
        except Exception as exc:
            logger.error("No config file,", exc)
            raise ExtractorConfigFileNotFoundError

        self.__tv_series_names = []
        self.__headless = True
        self.__serialization = True
        self.__serialization_fname = "src/pickle"

        if 'tv_series' not in cfg:
            self.__tv_series_names = []
        else:
            self.__tv_series_names = cfg['tv_series']

        if 'headless' in cfg:
            self.__headless = cfg['headless']

        if 'pickle' in cfg:
            if 'should_pickle' in cfg['pickle']:
                self.__serialization = cfg['pickle']['should_pickle']
            if 'pickle_filename' in cfg['pickle']:
                self.__serialization_fname = cfg['pickle']['pickle_filename']

    @property
    def should_serialize(self) -> bool:
        """Returns if serialization is on or off, default to on if not
        specified in config."""
        return self.__serialization

    @property
    def serialization_filename(self) -> str:
        """Returns the filename used for serialization, default to None if
        serialization is off."""
        if not self.__serialization:
            return None
        else:
            return self.__serialization_fname

    @property
    def tv_series_names(self):
        return self.__tv_series_names

    @property
    def headless(self):
        return self.__headless
