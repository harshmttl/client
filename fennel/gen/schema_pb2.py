# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x13\x66\x65nnel.proto.schema\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa8\x05\n\x08\x44\x61taType\x12\x30\n\x08int_type\x18\x01 \x01(\x0b\x32\x1c.fennel.proto.schema.IntTypeH\x00\x12\x36\n\x0b\x64ouble_type\x18\x02 \x01(\x0b\x32\x1f.fennel.proto.schema.DoubleTypeH\x00\x12\x36\n\x0bstring_type\x18\x03 \x01(\x0b\x32\x1f.fennel.proto.schema.StringTypeH\x00\x12\x32\n\tbool_type\x18\x04 \x01(\x0b\x32\x1d.fennel.proto.schema.BoolTypeH\x00\x12<\n\x0etimestamp_type\x18\x05 \x01(\x0b\x32\".fennel.proto.schema.TimestampTypeH\x00\x12\x34\n\narray_type\x18\x06 \x01(\x0b\x32\x1e.fennel.proto.schema.ArrayTypeH\x00\x12\x30\n\x08map_type\x18\x07 \x01(\x0b\x32\x1c.fennel.proto.schema.MapTypeH\x00\x12<\n\x0e\x65mbedding_type\x18\x08 \x01(\x0b\x32\".fennel.proto.schema.EmbeddingTypeH\x00\x12\x34\n\x0c\x62\x65tween_type\x18\t \x01(\x0b\x32\x1c.fennel.proto.schema.BetweenH\x00\x12\x31\n\x0bone_of_type\x18\n \x01(\x0b\x32\x1a.fennel.proto.schema.OneOfH\x00\x12\x34\n\nregex_type\x18\x0b \x01(\x0b\x32\x1e.fennel.proto.schema.RegexTypeH\x00\x12:\n\roptional_type\x18\x0c \x01(\x0b\x32!.fennel.proto.schema.OptionalTypeH\x00\x42\x07\n\x05\x64type\"\t\n\x07IntType\"\x0c\n\nDoubleType\"\x0c\n\nStringType\"\n\n\x08\x42oolType\"\x0f\n\rTimestampType\"\x1c\n\tRegexType\x12\x0f\n\x07pattern\x18\x01 \x01(\t\"6\n\tArrayType\x12)\n\x02of\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\"\'\n\rEmbeddingType\x12\x16\n\x0e\x65mbedding_size\x18\x02 \x01(\x05\"c\n\x07MapType\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\"\xb1\x01\n\x07\x42\x65tween\x12,\n\x05\x64type\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12\'\n\x03min\x18\x02 \x01(\x0b\x32\x1a.fennel.proto.schema.Value\x12\'\n\x03max\x18\x03 \x01(\x0b\x32\x1a.fennel.proto.schema.Value\x12\x12\n\nstrict_min\x18\x04 \x01(\x08\x12\x12\n\nstrict_max\x18\x05 \x01(\x08\"_\n\x05OneOf\x12)\n\x02of\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12+\n\x07options\x18\x02 \x03(\x0b\x32\x1a.fennel.proto.schema.Value\"9\n\x0cOptionalType\x12)\n\x02of\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\"C\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x05\x64type\x18\x02 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\"4\n\x06Schema\x12*\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x1a.fennel.proto.schema.Field\"u\n\x08\x44SSchema\x12)\n\x04keys\x18\x01 \x01(\x0b\x32\x1b.fennel.proto.schema.Schema\x12+\n\x06values\x18\x02 \x01(\x0b\x32\x1b.fennel.proto.schema.Schema\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"\xb9\x02\n\x05Value\x12)\n\x04none\x18\x01 \x01(\x0b\x32\x19.fennel.proto.schema.NoneH\x00\x12\x0e\n\x04\x62ool\x18\x02 \x01(\x08H\x00\x12\r\n\x03int\x18\x03 \x01(\x03H\x00\x12\x0f\n\x05\x66loat\x18\x04 \x01(\x01H\x00\x12\x10\n\x06string\x18\x05 \x01(\tH\x00\x12/\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x33\n\tembedding\x18\x07 \x01(\x0b\x32\x1e.fennel.proto.schema.EmbeddingH\x00\x12)\n\x04list\x18\x08 \x01(\x0b\x32\x19.fennel.proto.schema.ListH\x00\x12\'\n\x03map\x18\t \x01(\x0b\x32\x18.fennel.proto.schema.MapH\x00\x42\t\n\x07variant\"\x1b\n\tEmbedding\x12\x0e\n\x06values\x18\x01 \x03(\x01\"`\n\x04List\x12,\n\x05\x64type\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12*\n\x06values\x18\x02 \x03(\x0b\x32\x1a.fennel.proto.schema.Value\"\xf9\x01\n\x03Map\x12\x30\n\tkey_dtype\x18\x01 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12\x32\n\x0bvalue_dtype\x18\x02 \x01(\x0b\x32\x1d.fennel.proto.schema.DataType\x12/\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x1e.fennel.proto.schema.Map.Entry\x1a[\n\x05\x45ntry\x12\'\n\x03key\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Value\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.fennel.proto.schema.Value\"\x06\n\x04Noneb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATATYPE._serialized_start=71
  _DATATYPE._serialized_end=751
  _INTTYPE._serialized_start=753
  _INTTYPE._serialized_end=762
  _DOUBLETYPE._serialized_start=764
  _DOUBLETYPE._serialized_end=776
  _STRINGTYPE._serialized_start=778
  _STRINGTYPE._serialized_end=790
  _BOOLTYPE._serialized_start=792
  _BOOLTYPE._serialized_end=802
  _TIMESTAMPTYPE._serialized_start=804
  _TIMESTAMPTYPE._serialized_end=819
  _REGEXTYPE._serialized_start=821
  _REGEXTYPE._serialized_end=849
  _ARRAYTYPE._serialized_start=851
  _ARRAYTYPE._serialized_end=905
  _EMBEDDINGTYPE._serialized_start=907
  _EMBEDDINGTYPE._serialized_end=946
  _MAPTYPE._serialized_start=948
  _MAPTYPE._serialized_end=1047
  _BETWEEN._serialized_start=1050
  _BETWEEN._serialized_end=1227
  _ONEOF._serialized_start=1229
  _ONEOF._serialized_end=1324
  _OPTIONALTYPE._serialized_start=1326
  _OPTIONALTYPE._serialized_end=1383
  _FIELD._serialized_start=1385
  _FIELD._serialized_end=1452
  _SCHEMA._serialized_start=1454
  _SCHEMA._serialized_end=1506
  _DSSCHEMA._serialized_start=1508
  _DSSCHEMA._serialized_end=1625
  _VALUE._serialized_start=1628
  _VALUE._serialized_end=1941
  _EMBEDDING._serialized_start=1943
  _EMBEDDING._serialized_end=1970
  _LIST._serialized_start=1972
  _LIST._serialized_end=2068
  _MAP._serialized_start=2071
  _MAP._serialized_end=2320
  _MAP_ENTRY._serialized_start=2229
  _MAP_ENTRY._serialized_end=2320
  _NONE._serialized_start=2322
  _NONE._serialized_end=2328
# @@protoc_insertion_point(module_scope)
