# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.schema_pb2 as schema__pb2
import fennel.gen.status_pb2 as status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rfeature.proto\x12\x0c\x66\x65nnel.proto\x1a\x0cschema.proto\x1a\x0cstatus.proto"\x81\x02\n\x14\x43reateFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\t\x12*\n\x04type\x18\x03 \x01(\x0e\x32\x1c.fennel.proto.FeatureDefType\x12\x0f\n\x07version\x18\x04 \x01(\r\x12\x10\n\x08\x66unction\x18\x05 \x01(\x0c\x12\x1c\n\x14\x66unction_source_code\x18\x06 \x01(\t\x12\x1d\n\x15\x64\x65pends_on_aggregates\x18\x07 \x03(\t\x12\x1b\n\x13\x64\x65pends_on_features\x18\x08 \x03(\t\x12$\n\x06schema\x18\t \x01(\x0b\x32\x14.fennel.proto.Schema"\xb3\x01\n\x16\x45xtractFeaturesRequest\x12\x15\n\rfeature_names\x18\x01 \x03(\t\x12\x11\n\tdataframe\x18\x02 \x01(\x0c\x12@\n\x06\x63onfig\x18\x03 \x03(\x0b\x32\x30.fennel.proto.ExtractFeaturesRequest.ConfigEntry\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01"?\n\x17\x45xtractFeaturesResponse\x12$\n\x06status\x18\x01 \x01(\x0b\x32\x14.fennel.proto.Status*/\n\x0e\x46\x65\x61tureDefType\x12\x0b\n\x07\x46\x45\x41TURE\x10\x00\x12\x10\n\x0c\x46\x45\x41TURE_PACK\x10\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "feature_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _EXTRACTFEATURESREQUEST_CONFIGENTRY._options = None
    _EXTRACTFEATURESREQUEST_CONFIGENTRY._serialized_options = b"8\001"
    _FEATUREDEFTYPE._serialized_start = 566
    _FEATUREDEFTYPE._serialized_end = 613
    _CREATEFEATUREREQUEST._serialized_start = 60
    _CREATEFEATUREREQUEST._serialized_end = 317
    _EXTRACTFEATURESREQUEST._serialized_start = 320
    _EXTRACTFEATURESREQUEST._serialized_end = 499
    _EXTRACTFEATURESREQUEST_CONFIGENTRY._serialized_start = 454
    _EXTRACTFEATURESREQUEST_CONFIGENTRY._serialized_end = 499
    _EXTRACTFEATURESRESPONSE._serialized_start = 501
    _EXTRACTFEATURESRESPONSE._serialized_end = 564
# @@protoc_insertion_point(module_scope)
