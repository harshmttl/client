# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.featureset_pb2 as featureset__pb2
import fennel.gen.dataset_pb2 as dataset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservices.proto\x12\x0c\x66\x65nnel.proto\x1a\x10\x66\x65\x61tureset.proto\x1a\rdataset.proto\"\x8f\x01\n\x0bSyncRequest\x12<\n\x10\x64\x61taset_requests\x18\x01 \x03(\x0b\x32\".fennel.proto.CreateDatasetRequest\x12\x42\n\x13\x66\x65\x61tureset_requests\x18\x03 \x03(\x0b\x32%.fennel.proto.CreateFeaturesetRequest\"\x95\x01\n\x0cSyncResponse\x12>\n\x11\x64\x61taset_responses\x18\x01 \x03(\x0b\x32#.fennel.proto.CreateDatasetResponse\x12\x45\n\x15\x66\x65\x61ture_set_responses\x18\x03 \x03(\x0b\x32&.fennel.proto.CreateFeatureSetResponse2S\n\x12\x46\x65nnelFeatureStore\x12=\n\x04Sync\x12\x19.fennel.proto.SyncRequest\x1a\x1a.fennel.proto.SyncResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYNCREQUEST._serialized_start=66
  _SYNCREQUEST._serialized_end=209
  _SYNCRESPONSE._serialized_start=212
  _SYNCRESPONSE._serialized_end=361
  _FENNELFEATURESTORE._serialized_start=363
  _FENNELFEATURESTORE._serialized_end=446
# @@protoc_insertion_point(module_scope)
