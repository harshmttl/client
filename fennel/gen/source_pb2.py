# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csource.proto\x12\x0c\x66\x65nnel.proto\"\xae\x01\n\rDataConnector\x12(\n\x06source\x18\x01 \x01(\x0b\x32\x18.fennel.proto.DataSource\x12\x14\n\x0c\x63ursor_field\x18\x02 \x01(\t\x12\x0f\n\x05table\x18\x03 \x01(\tH\x00\x12\x31\n\x0cs3_connector\x18\x04 \x01(\x0b\x32\x19.fennel.proto.S3ConnectorH\x00\x12\r\n\x05\x65very\x18\x05 \x01(\x05\x42\n\n\x08instance\"\xc0\x01\n\nDataSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12 \n\x03sql\x18\x02 \x01(\x0b\x32\x11.fennel.proto.SQLH\x00\x12\x1e\n\x02s3\x18\x03 \x01(\x0b\x32\x10.fennel.proto.S3H\x00\x12*\n\x08\x62igquery\x18\x04 \x01(\x0b\x32\x16.fennel.proto.BigQueryH\x00\x12,\n\tsnowflake\x18\x05 \x01(\x0b\x32\x17.fennel.proto.SnowflakeH\x00\x42\x08\n\x06source\"\xb7\x01\n\x03SQL\x12+\n\x08sql_type\x18\x01 \x01(\x0e\x32\x19.fennel.proto.SQL.SQLType\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\n\n\x02\x64\x62\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\r\x12\x13\n\x0bjdbc_params\x18\x07 \x01(\t\"\"\n\x07SQLType\x12\x0c\n\x08Postgres\x10\x00\x12\t\n\x05MySQL\x10\x01\">\n\x02S3\x12\x19\n\x11\x61ws_access_key_id\x18\x01 \x01(\t\x12\x1d\n\x15\x61ws_secret_access_key\x18\x02 \x01(\t\"\xbb\x01\n\x0bS3Connector\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x13\n\x0bpath_prefix\x18\x02 \x01(\t\x12\x35\n\x06schema\x18\x03 \x03(\x0b\x32%.fennel.proto.S3Connector.SchemaEntry\x12\x11\n\tdelimiter\x18\x04 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x05 \x01(\t\x1a-\n\x0bSchemaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x08\x42igQuery\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\x18\n\x10\x63redentials_json\x18\x03 \x01(\t\"\x92\x01\n\tSnowflake\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\n\n\x02\x64\x62\x18\x04 \x01(\t\x12\x0e\n\x06schema\x18\x05 \x01(\t\x12\x11\n\twarehouse\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12\x13\n\x0bjdbc_params\x18\x08 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'source_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _S3CONNECTOR_SCHEMAENTRY._options = None
  _S3CONNECTOR_SCHEMAENTRY._serialized_options = b'8\001'
  _DATACONNECTOR._serialized_start=31
  _DATACONNECTOR._serialized_end=205
  _DATASOURCE._serialized_start=208
  _DATASOURCE._serialized_end=400
  _SQL._serialized_start=403
  _SQL._serialized_end=586
  _SQL_SQLTYPE._serialized_start=552
  _SQL_SQLTYPE._serialized_end=586
  _S3._serialized_start=588
  _S3._serialized_end=650
  _S3CONNECTOR._serialized_start=653
  _S3CONNECTOR._serialized_end=840
  _S3CONNECTOR_SCHEMAENTRY._serialized_start=795
  _S3CONNECTOR_SCHEMAENTRY._serialized_end=840
  _BIGQUERY._serialized_start=842
  _BIGQUERY._serialized_end=915
  _SNOWFLAKE._serialized_start=918
  _SNOWFLAKE._serialized_end=1064
# @@protoc_insertion_point(module_scope)
