# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: format.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x66ormat.proto\x12\x13\x66\x65nnel.proto.format\"\xb4\x03\n\nFileFormat\x12:\n\x07parquet\x18\x01 \x01(\x0b\x32\'.fennel.proto.format.FileFormat.ParquetH\x00\x12\x34\n\x04json\x18\x02 \x01(\x0b\x32$.fennel.proto.format.FileFormat.JsonH\x00\x12\x34\n\x04\x61vro\x18\x03 \x01(\x0b\x32$.fennel.proto.format.FileFormat.AvroH\x00\x12\x34\n\x04hudi\x18\x04 \x01(\x0b\x32$.fennel.proto.format.FileFormat.HudiH\x00\x12\x41\n\x0b\x64\x65lta_table\x18\x05 \x01(\x0b\x32*.fennel.proto.format.FileFormat.DeltaTableH\x00\x12\x32\n\x03\x63sv\x18\x06 \x01(\x0b\x32#.fennel.proto.format.FileFormat.CSVH\x00\x1a\t\n\x07Parquet\x1a\x06\n\x04Json\x1a\x06\n\x04\x41vro\x1a\x06\n\x04Hudi\x1a\x0c\n\nDeltaTable\x1a\x18\n\x03\x43SV\x12\x11\n\tdelimiter\x18\x01 \x01(\x0c\x42\x06\n\x04kindb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'format_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_FILEFORMAT']._serialized_start=38
  _globals['_FILEFORMAT']._serialized_end=474
  _globals['_FILEFORMAT_PARQUET']._serialized_start=393
  _globals['_FILEFORMAT_PARQUET']._serialized_end=402
  _globals['_FILEFORMAT_JSON']._serialized_start=404
  _globals['_FILEFORMAT_JSON']._serialized_end=410
  _globals['_FILEFORMAT_AVRO']._serialized_start=412
  _globals['_FILEFORMAT_AVRO']._serialized_end=418
  _globals['_FILEFORMAT_HUDI']._serialized_start=420
  _globals['_FILEFORMAT_HUDI']._serialized_end=426
  _globals['_FILEFORMAT_DELTATABLE']._serialized_start=428
  _globals['_FILEFORMAT_DELTATABLE']._serialized_end=440
  _globals['_FILEFORMAT_CSV']._serialized_start=442
  _globals['_FILEFORMAT_CSV']._serialized_end=466
# @@protoc_insertion_point(module_scope)