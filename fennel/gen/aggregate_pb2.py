# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aggregate.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61ggregate.proto\x12\x0c\x66\x65nnel.proto\x1a\x0cschema.proto\"\xde\x01\n\x16\x43reateAggregateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\r\x12\x0e\n\x06stream\x18\x04 \x01(\t\x12\x1b\n\x13preprocess_function\x18\x05 \x01(\x0c\x12\x33\n\x0e\x61ggregate_type\x18\x06 \x01(\x0e\x32\x1b.fennel.proto.AggregateType\x12\x0f\n\x07windows\x18\x07 \x03(\x05\x12$\n\x06schema\x18\x08 \x01(\x0b\x32\x14.fennel.proto.Schema*W\n\rAggregateType\x12\x07\n\x03SUM\x10\x00\x12\x07\n\x03\x41VG\x10\x01\x12\t\n\x05\x43OUNT\x10\x02\x12\x07\n\x03MIN\x10\x03\x12\x07\n\x03MAX\x10\x04\x12\x08\n\x04RATE\x10\x05\x12\r\n\tKEY_VALUE\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aggregate_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AGGREGATETYPE._serialized_start=272
  _AGGREGATETYPE._serialized_end=359
  _CREATEAGGREGATEREQUEST._serialized_start=48
  _CREATEAGGREGATEREQUEST._serialized_end=270
# @@protoc_insertion_point(module_scope)
