# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: expectations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.metadata_pb2 as metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x65xpectations.proto\x12\x19\x66\x65nnel.proto.expectations\x1a\x0emetadata.proto\"\xc9\x02\n\x0c\x45xpectations\x12\x13\n\x0b\x65ntity_name\x18\x01 \x01(\t\x12\x16\n\x0e\x65ntity_version\x18\x02 \x01(\x05\x12\r\n\x05suite\x18\x03 \x01(\t\x12<\n\x0c\x65xpectations\x18\x04 \x03(\x0b\x32&.fennel.proto.expectations.Expectation\x12\x0f\n\x07version\x18\x05 \x01(\x05\x12\x31\n\x08metadata\x18\x06 \x01(\x0b\x32\x1f.fennel.proto.metadata.Metadata\x12\x42\n\x06\x65_type\x18\x07 \x01(\x0e\x32\x32.fennel.proto.expectations.Expectations.EntityType\x12\x0c\n\x04tags\x18\x08 \x03(\t\")\n\nEntityType\x12\x0b\n\x07\x44\x61taset\x10\x00\x12\x0e\n\nFeatureset\x10\x01\"C\n\x0b\x45xpectation\x12\x18\n\x10\x65xpectation_type\x18\x01 \x01(\t\x12\x1a\n\x12\x65xpectation_kwargs\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'expectations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXPECTATIONS._serialized_start=66
  _EXPECTATIONS._serialized_end=395
  _EXPECTATIONS_ENTITYTYPE._serialized_start=354
  _EXPECTATIONS_ENTITYTYPE._serialized_end=395
  _EXPECTATION._serialized_start=397
  _EXPECTATION._serialized_end=464
# @@protoc_insertion_point(module_scope)
