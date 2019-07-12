# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imdb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imdb.proto',
  package='imdb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nimdb.proto\x12\x04imdb\"%\n\x12GenericShowRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\t\"&\n\x11\x43reateShowRequest\x12\x11\n\titem_name\x18\x01 \x01(\t\"L\n\x12\x43reateShowResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\x12\x0f\n\x07item_id\x18\x02 \x01(\t\x12\x14\n\x0ctime_created\x18\x03 \x01(\t\"\x17\n\x04Show\x12\x0f\n\x07item_id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"&\n\x11\x45xtractionRequest\x12\x11\n\titem_name\x18\x01 \x01(\t\"D\n\x12\x45xtractionResponse\x12\x1a\n\x12is_item_name_valid\x18\x01 \x01(\x08\x12\x12\n\nsuccessful\x18\x02 \x01(\x08\"\'\n\x10\x43reateJobRequest\x12\x13\n\x0btarget_name\x18\x01 \x01(\t\"\'\n\x11\x43reateJobResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\"&\n\x10\x44\x65leteJobRequest\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\"$\n\rGetJobRequest\x12\x13\n\x0btarget_name\x18\x01 \x01(\t\"&\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0btarget_name\x18\x02 \x01(\t\"$\n\x11PredictionRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\t\"/\n\x12PredictionResponse\x12\x19\n\x11is_resource_valid\x18\x01 \x01(\x08\x32\xbe\x01\n\x0f\x44\x61tabaseService\x12\x31\n\x07GetShow\x12\x18.imdb.GenericShowRequest\x1a\n.imdb.Show\"\x00\x12\x41\n\nCreateShow\x12\x17.imdb.CreateShowRequest\x1a\x18.imdb.CreateShowResponse\"\x00\x12\x35\n\nDeleteShow\x12\x18.imdb.GenericShowRequest\x1a\x0b.imdb.Empty\"\x00\x32]\n\x10\x45xtractorService\x12I\n\x12InitiateExtraction\x12\x17.imdb.ExtractionRequest\x1a\x18.imdb.ExtractionResponse\"\x00\x32\xac\x01\n\nJobService\x12>\n\tCreateJob\x12\x16.imdb.CreateJobRequest\x1a\x17.imdb.CreateJobResponse\"\x00\x12*\n\x06GetJob\x12\x13.imdb.GetJobRequest\x1a\t.imdb.Job\"\x00\x12\x32\n\tDeleteJob\x12\x16.imdb.DeleteJobRequest\x1a\x0b.imdb.Empty\"\x00\x32\x17\n\x15RecommendationService2_\n\x17RatingPredictionService\x12\x44\n\rPredictRating\x12\x17.imdb.PredictionRequest\x1a\x18.imdb.PredictionResponse\"\x00\x62\x06proto3')
)




_GENERICSHOWREQUEST = _descriptor.Descriptor(
  name='GenericShowRequest',
  full_name='imdb.GenericShowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='imdb.GenericShowRequest.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=57,
)


_CREATESHOWREQUEST = _descriptor.Descriptor(
  name='CreateShowRequest',
  full_name='imdb.CreateShowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_name', full_name='imdb.CreateShowRequest.item_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=97,
)


_CREATESHOWRESPONSE = _descriptor.Descriptor(
  name='CreateShowResponse',
  full_name='imdb.CreateShowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='imdb.CreateShowResponse.created', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='imdb.CreateShowResponse.item_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_created', full_name='imdb.CreateShowResponse.time_created', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=175,
)


_SHOW = _descriptor.Descriptor(
  name='Show',
  full_name='imdb.Show',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='imdb.Show.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=200,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='imdb.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=209,
)


_EXTRACTIONREQUEST = _descriptor.Descriptor(
  name='ExtractionRequest',
  full_name='imdb.ExtractionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_name', full_name='imdb.ExtractionRequest.item_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=249,
)


_EXTRACTIONRESPONSE = _descriptor.Descriptor(
  name='ExtractionResponse',
  full_name='imdb.ExtractionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_item_name_valid', full_name='imdb.ExtractionResponse.is_item_name_valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='successful', full_name='imdb.ExtractionResponse.successful', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=319,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='imdb.CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_name', full_name='imdb.CreateJobRequest.target_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=360,
)


_CREATEJOBRESPONSE = _descriptor.Descriptor(
  name='CreateJobResponse',
  full_name='imdb.CreateJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='imdb.CreateJobResponse.successful', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=401,
)


_DELETEJOBREQUEST = _descriptor.Descriptor(
  name='DeleteJobRequest',
  full_name='imdb.DeleteJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='imdb.DeleteJobRequest.successful', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=441,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='imdb.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_name', full_name='imdb.GetJobRequest.target_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=479,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='imdb.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='imdb.Job.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_name', full_name='imdb.Job.target_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=519,
)


_PREDICTIONREQUEST = _descriptor.Descriptor(
  name='PredictionRequest',
  full_name='imdb.PredictionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='imdb.PredictionRequest.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=557,
)


_PREDICTIONRESPONSE = _descriptor.Descriptor(
  name='PredictionResponse',
  full_name='imdb.PredictionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_resource_valid', full_name='imdb.PredictionResponse.is_resource_valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=606,
)

DESCRIPTOR.message_types_by_name['GenericShowRequest'] = _GENERICSHOWREQUEST
DESCRIPTOR.message_types_by_name['CreateShowRequest'] = _CREATESHOWREQUEST
DESCRIPTOR.message_types_by_name['CreateShowResponse'] = _CREATESHOWRESPONSE
DESCRIPTOR.message_types_by_name['Show'] = _SHOW
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['ExtractionRequest'] = _EXTRACTIONREQUEST
DESCRIPTOR.message_types_by_name['ExtractionResponse'] = _EXTRACTIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['CreateJobResponse'] = _CREATEJOBRESPONSE
DESCRIPTOR.message_types_by_name['DeleteJobRequest'] = _DELETEJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['PredictionRequest'] = _PREDICTIONREQUEST
DESCRIPTOR.message_types_by_name['PredictionResponse'] = _PREDICTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericShowRequest = _reflection.GeneratedProtocolMessageType('GenericShowRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERICSHOWREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.GenericShowRequest)
  })
_sym_db.RegisterMessage(GenericShowRequest)

CreateShowRequest = _reflection.GeneratedProtocolMessageType('CreateShowRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESHOWREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.CreateShowRequest)
  })
_sym_db.RegisterMessage(CreateShowRequest)

CreateShowResponse = _reflection.GeneratedProtocolMessageType('CreateShowResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESHOWRESPONSE,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.CreateShowResponse)
  })
_sym_db.RegisterMessage(CreateShowResponse)

Show = _reflection.GeneratedProtocolMessageType('Show', (_message.Message,), {
  'DESCRIPTOR' : _SHOW,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.Show)
  })
_sym_db.RegisterMessage(Show)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.Empty)
  })
_sym_db.RegisterMessage(Empty)

ExtractionRequest = _reflection.GeneratedProtocolMessageType('ExtractionRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTIONREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.ExtractionRequest)
  })
_sym_db.RegisterMessage(ExtractionRequest)

ExtractionResponse = _reflection.GeneratedProtocolMessageType('ExtractionResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTIONRESPONSE,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.ExtractionResponse)
  })
_sym_db.RegisterMessage(ExtractionResponse)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

CreateJobResponse = _reflection.GeneratedProtocolMessageType('CreateJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBRESPONSE,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.CreateJobResponse)
  })
_sym_db.RegisterMessage(CreateJobResponse)

DeleteJobRequest = _reflection.GeneratedProtocolMessageType('DeleteJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEJOBREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.DeleteJobRequest)
  })
_sym_db.RegisterMessage(DeleteJobRequest)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.Job)
  })
_sym_db.RegisterMessage(Job)

PredictionRequest = _reflection.GeneratedProtocolMessageType('PredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.PredictionRequest)
  })
_sym_db.RegisterMessage(PredictionRequest)

PredictionResponse = _reflection.GeneratedProtocolMessageType('PredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONRESPONSE,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:imdb.PredictionResponse)
  })
_sym_db.RegisterMessage(PredictionResponse)



_DATABASESERVICE = _descriptor.ServiceDescriptor(
  name='DatabaseService',
  full_name='imdb.DatabaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=609,
  serialized_end=799,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetShow',
    full_name='imdb.DatabaseService.GetShow',
    index=0,
    containing_service=None,
    input_type=_GENERICSHOWREQUEST,
    output_type=_SHOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateShow',
    full_name='imdb.DatabaseService.CreateShow',
    index=1,
    containing_service=None,
    input_type=_CREATESHOWREQUEST,
    output_type=_CREATESHOWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteShow',
    full_name='imdb.DatabaseService.DeleteShow',
    index=2,
    containing_service=None,
    input_type=_GENERICSHOWREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABASESERVICE)

DESCRIPTOR.services_by_name['DatabaseService'] = _DATABASESERVICE


_EXTRACTORSERVICE = _descriptor.ServiceDescriptor(
  name='ExtractorService',
  full_name='imdb.ExtractorService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=801,
  serialized_end=894,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitiateExtraction',
    full_name='imdb.ExtractorService.InitiateExtraction',
    index=0,
    containing_service=None,
    input_type=_EXTRACTIONREQUEST,
    output_type=_EXTRACTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXTRACTORSERVICE)

DESCRIPTOR.services_by_name['ExtractorService'] = _EXTRACTORSERVICE


_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='JobService',
  full_name='imdb.JobService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=897,
  serialized_end=1069,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='imdb.JobService.CreateJob',
    index=0,
    containing_service=None,
    input_type=_CREATEJOBREQUEST,
    output_type=_CREATEJOBRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='imdb.JobService.GetJob',
    index=1,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteJob',
    full_name='imdb.JobService.DeleteJob',
    index=2,
    containing_service=None,
    input_type=_DELETEJOBREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['JobService'] = _JOBSERVICE


_RECOMMENDATIONSERVICE = _descriptor.ServiceDescriptor(
  name='RecommendationService',
  full_name='imdb.RecommendationService',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  serialized_start=1071,
  serialized_end=1094,
  methods=[
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDATIONSERVICE)

DESCRIPTOR.services_by_name['RecommendationService'] = _RECOMMENDATIONSERVICE


_RATINGPREDICTIONSERVICE = _descriptor.ServiceDescriptor(
  name='RatingPredictionService',
  full_name='imdb.RatingPredictionService',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  serialized_start=1096,
  serialized_end=1191,
  methods=[
  _descriptor.MethodDescriptor(
    name='PredictRating',
    full_name='imdb.RatingPredictionService.PredictRating',
    index=0,
    containing_service=None,
    input_type=_PREDICTIONREQUEST,
    output_type=_PREDICTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RATINGPREDICTIONSERVICE)

DESCRIPTOR.services_by_name['RatingPredictionService'] = _RATINGPREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)