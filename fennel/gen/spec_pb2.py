# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spec.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.window_pb2 as window__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nspec.proto\x12\x11\x66\x65nnel.proto.spec\x1a\x0cwindow.proto\"\x95\x01\n\x07PreSpec\x12%\n\x03sum\x18\x01 \x01(\x0b\x32\x16.fennel.proto.spec.SumH\x00\x12-\n\x07\x61verage\x18\x02 \x01(\x0b\x32\x1a.fennel.proto.spec.AverageH\x00\x12)\n\x05\x63ount\x18\x03 \x01(\x0b\x32\x18.fennel.proto.spec.CountH\x00\x42\t\n\x07variant\"L\n\x03Sum\x12\n\n\x02of\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\"a\n\x07\x41verage\x12\n\n\x02of\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x01\"B\n\x05\x43ount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x06window\x18\x02 \x01(\x0b\x32\x1b.fennel.proto.window.Windowb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spec_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRESPEC._serialized_start=48
  _PRESPEC._serialized_end=197
  _SUM._serialized_start=199
  _SUM._serialized_end=275
  _AVERAGE._serialized_start=277
  _AVERAGE._serialized_end=374
  _COUNT._serialized_start=376
  _COUNT._serialized_end=442
# @@protoc_insertion_point(module_scope)
