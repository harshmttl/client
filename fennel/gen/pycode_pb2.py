# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pycode.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpycode.proto\x12\x13\x66\x65nnel.proto.pycode\"\xb3\x02\n\x06PyCode\x12\x13\n\x0b\x65ntry_point\x18\x01 \x01(\t\x12\x13\n\x0bsource_code\x18\x02 \x01(\t\x12\x11\n\tcore_code\x18\x03 \x01(\t\x12\x16\n\x0egenerated_code\x18\x04 \x01(\t\x12-\n\x08includes\x18\x05 \x03(\x0b\x32\x1b.fennel.proto.pycode.PyCode\x12\x42\n\x0cref_includes\x18\x06 \x03(\x0b\x32,.fennel.proto.pycode.PyCode.RefIncludesEntry\x12\x0f\n\x07imports\x18\x07 \x01(\t\x1aP\n\x10RefIncludesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0e\x32\x1c.fennel.proto.pycode.RefType:\x02\x38\x01*&\n\x07RefType\x12\x0b\n\x07\x44\x61taset\x10\x00\x12\x0e\n\nFeatureset\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pycode_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PYCODE_REFINCLUDESENTRY']._options = None
  _globals['_PYCODE_REFINCLUDESENTRY']._serialized_options = b'8\001'
  _globals['_REFTYPE']._serialized_start=347
  _globals['_REFTYPE']._serialized_end=385
  _globals['_PYCODE']._serialized_start=38
  _globals['_PYCODE']._serialized_end=345
  _globals['_PYCODE_REFINCLUDESENTRY']._serialized_start=265
  _globals['_PYCODE_REFINCLUDESENTRY']._serialized_end=345
# @@protoc_insertion_point(module_scope)
