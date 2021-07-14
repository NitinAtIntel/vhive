# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: videoservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='videoservice.proto',
  package='videoservice',
  syntax='proto3',
  serialized_options=b'\n\031com.vhive.video_analyticsB\014videoserviceP\001Z\033tests/video_analytics/proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12videoservice.proto\x12\x0cvideoservice\"\x1e\n\rDecodeRequest\x12\r\n\x05video\x18\x01 \x01(\x0c\"%\n\x0b\x44\x65\x63odeReply\x12\x16\n\x0e\x63lassification\x18\x01 \x01(\t\"!\n\x10RecogniseRequest\x12\r\n\x05\x66rame\x18\x01 \x01(\x0c\"(\n\x0eRecogniseReply\x12\x16\n\x0e\x63lassification\x18\x01 \x01(\t2R\n\x0cVideoDecoder\x12\x42\n\x06\x44\x65\x63ode\x12\x1b.videoservice.DecodeRequest\x1a\x19.videoservice.DecodeReply\"\x00\x32`\n\x11ObjectRecognition\x12K\n\tRecognise\x12\x1e.videoservice.RecogniseRequest\x1a\x1c.videoservice.RecogniseReply\"\x00\x42H\n\x19\x63om.vhive.video_analyticsB\x0cvideoserviceP\x01Z\x1btests/video_analytics/protob\x06proto3'
)




_DECODEREQUEST = _descriptor.Descriptor(
  name='DecodeRequest',
  full_name='videoservice.DecodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='video', full_name='videoservice.DecodeRequest.video', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=36,
  serialized_end=66,
)


_DECODEREPLY = _descriptor.Descriptor(
  name='DecodeReply',
  full_name='videoservice.DecodeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification', full_name='videoservice.DecodeReply.classification', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=68,
  serialized_end=105,
)


_RECOGNISEREQUEST = _descriptor.Descriptor(
  name='RecogniseRequest',
  full_name='videoservice.RecogniseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='videoservice.RecogniseRequest.frame', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=107,
  serialized_end=140,
)


_RECOGNISEREPLY = _descriptor.Descriptor(
  name='RecogniseReply',
  full_name='videoservice.RecogniseReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification', full_name='videoservice.RecogniseReply.classification', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=142,
  serialized_end=182,
)

DESCRIPTOR.message_types_by_name['DecodeRequest'] = _DECODEREQUEST
DESCRIPTOR.message_types_by_name['DecodeReply'] = _DECODEREPLY
DESCRIPTOR.message_types_by_name['RecogniseRequest'] = _RECOGNISEREQUEST
DESCRIPTOR.message_types_by_name['RecogniseReply'] = _RECOGNISEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DecodeRequest = _reflection.GeneratedProtocolMessageType('DecodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECODEREQUEST,
  '__module__' : 'videoservice_pb2'
  # @@protoc_insertion_point(class_scope:videoservice.DecodeRequest)
  })
_sym_db.RegisterMessage(DecodeRequest)

DecodeReply = _reflection.GeneratedProtocolMessageType('DecodeReply', (_message.Message,), {
  'DESCRIPTOR' : _DECODEREPLY,
  '__module__' : 'videoservice_pb2'
  # @@protoc_insertion_point(class_scope:videoservice.DecodeReply)
  })
_sym_db.RegisterMessage(DecodeReply)

RecogniseRequest = _reflection.GeneratedProtocolMessageType('RecogniseRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNISEREQUEST,
  '__module__' : 'videoservice_pb2'
  # @@protoc_insertion_point(class_scope:videoservice.RecogniseRequest)
  })
_sym_db.RegisterMessage(RecogniseRequest)

RecogniseReply = _reflection.GeneratedProtocolMessageType('RecogniseReply', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNISEREPLY,
  '__module__' : 'videoservice_pb2'
  # @@protoc_insertion_point(class_scope:videoservice.RecogniseReply)
  })
_sym_db.RegisterMessage(RecogniseReply)


DESCRIPTOR._options = None

_VIDEODECODER = _descriptor.ServiceDescriptor(
  name='VideoDecoder',
  full_name='videoservice.VideoDecoder',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=184,
  serialized_end=266,
  methods=[
  _descriptor.MethodDescriptor(
    name='Decode',
    full_name='videoservice.VideoDecoder.Decode',
    index=0,
    containing_service=None,
    input_type=_DECODEREQUEST,
    output_type=_DECODEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VIDEODECODER)

DESCRIPTOR.services_by_name['VideoDecoder'] = _VIDEODECODER


_OBJECTRECOGNITION = _descriptor.ServiceDescriptor(
  name='ObjectRecognition',
  full_name='videoservice.ObjectRecognition',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=268,
  serialized_end=364,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recognise',
    full_name='videoservice.ObjectRecognition.Recognise',
    index=0,
    containing_service=None,
    input_type=_RECOGNISEREQUEST,
    output_type=_RECOGNISEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBJECTRECOGNITION)

DESCRIPTOR.services_by_name['ObjectRecognition'] = _OBJECTRECOGNITION

# @@protoc_insertion_point(module_scope)
