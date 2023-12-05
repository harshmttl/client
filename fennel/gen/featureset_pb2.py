# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: featureset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.metadata_pb2 as metadata__pb2
import fennel.gen.schema_pb2 as schema__pb2
import fennel.gen.pycode_pb2 as pycode__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x66\x65\x61tureset.proto\x12\x17\x66\x65nnel.proto.featureset\x1a\x0emetadata.proto\x1a\x0cschema.proto\x1a\x0cpycode.proto\"\x8c\x01\n\x0e\x43oreFeatureset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x08metadata\x18\x02 \x01(\x0b\x32\x1f.fennel.proto.metadata.Metadata\x12+\n\x06pycode\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.pycode.PyCode\x12\x0c\n\x04tags\x18\x04 \x03(\t\"\xac\x01\n\x07\x46\x65\x61ture\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x05\x64type\x18\x03 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12\x31\n\x08metadata\x18\x04 \x01(\x0b\x32\x1f.fennel.proto.metadata.Metadata\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\"S\n\x0f\x46ieldLookupInfo\x12)\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\x12\x15\n\rdefault_value\x18\x03 \x01(\t\"\xa0\x03\n\tExtractor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tasets\x18\x02 \x03(\t\x12.\n\x06inputs\x18\x03 \x03(\x0b\x32\x1e.fennel.proto.featureset.Input\x12\x10\n\x08\x66\x65\x61tures\x18\x04 \x03(\t\x12\x31\n\x08metadata\x18\x05 \x01(\x0b\x32\x1f.fennel.proto.metadata.Metadata\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12+\n\x06pycode\x18\x07 \x01(\x0b\x32\x1b.fennel.proto.pycode.PyCode\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x08 \x01(\t\x12>\n\x0e\x65xtractor_type\x18\t \x01(\x0e\x32&.fennel.proto.featureset.ExtractorType\x12>\n\nfield_info\x18\n \x01(\x0b\x32(.fennel.proto.featureset.FieldLookupInfoH\x00\x12\x0c\n\x04tags\x18\x0b \x03(\tB\x18\n\x16\x64\x65rived_extractor_info\"s\n\x05Input\x12\x37\n\x07\x66\x65\x61ture\x18\x01 \x01(\x0b\x32&.fennel.proto.featureset.Input.Feature\x1a\x31\n\x07\x46\x65\x61ture\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xad\x01\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x06inputs\x18\x02 \x03(\x0b\x32 .fennel.proto.featureset.Feature\x12\x31\n\x07outputs\x18\x03 \x03(\x0b\x32 .fennel.proto.featureset.Feature\x12\x31\n\x08metadata\x18\x04 \x01(\x0b\x32\x1f.fennel.proto.metadata.Metadata*3\n\rExtractorType\x12\x0b\n\x07PY_FUNC\x10\x00\x12\n\n\x06LOOKUP\x10\x01\x12\t\n\x05\x41LIAS\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'featureset_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EXTRACTORTYPE']._serialized_start=1204
  _globals['_EXTRACTORTYPE']._serialized_end=1255
  _globals['_COREFEATURESET']._serialized_start=90
  _globals['_COREFEATURESET']._serialized_end=230
  _globals['_FEATURE']._serialized_start=233
  _globals['_FEATURE']._serialized_end=405
  _globals['_FIELDLOOKUPINFO']._serialized_start=407
  _globals['_FIELDLOOKUPINFO']._serialized_end=490
  _globals['_EXTRACTOR']._serialized_start=493
  _globals['_EXTRACTOR']._serialized_end=909
  _globals['_INPUT']._serialized_start=911
  _globals['_INPUT']._serialized_end=1026
  _globals['_INPUT_FEATURE']._serialized_start=977
  _globals['_INPUT_FEATURE']._serialized_end=1026
  _globals['_MODEL']._serialized_start=1029
  _globals['_MODEL']._serialized_end=1202
# @@protoc_insertion_point(module_scope)
