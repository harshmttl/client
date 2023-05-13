# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connector.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63onnector.proto\x12\x16\x66\x65nnel.proto.connector\x1a\x1egoogle/protobuf/duration.proto\"\xc0\x03\n\x0b\x45xtDatabase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x05mysql\x18\x02 \x01(\x0b\x32\x1d.fennel.proto.connector.MySQLH\x00\x12\x34\n\x08postgres\x18\x03 \x01(\x0b\x32 .fennel.proto.connector.PostgresH\x00\x12\x36\n\treference\x18\x04 \x01(\x0b\x32!.fennel.proto.connector.ReferenceH\x00\x12(\n\x02s3\x18\x05 \x01(\x0b\x32\x1a.fennel.proto.connector.S3H\x00\x12\x34\n\x08\x62igquery\x18\x06 \x01(\x0b\x32 .fennel.proto.connector.BigqueryH\x00\x12\x36\n\tsnowflake\x18\x07 \x01(\x0b\x32!.fennel.proto.connector.SnowflakeH\x00\x12.\n\x05kafka\x18\x08 \x01(\x0b\x32\x1d.fennel.proto.connector.KafkaH\x00\x12\x32\n\x07webhook\x18\t \x01(\x0b\x32\x1f.fennel.proto.connector.WebhookH\x00\x42\t\n\x07variant\"\xab\x01\n\tReference\x12;\n\x06\x64\x62type\x18\x01 \x01(\x0e\x32+.fennel.proto.connector.Reference.ExtDBType\"a\n\tExtDBType\x12\t\n\x05MYSQL\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\x06\n\x02S3\x10\x02\x12\t\n\x05KAFKA\x10\x03\x12\x0c\n\x08\x42IGQUERY\x10\x04\x12\r\n\tSNOWFLAKE\x10\x05\x12\x0b\n\x07WEBHOOK\x10\x06\"\x17\n\x07Webhook\x12\x0c\n\x04name\x18\x01 \x01(\t\"j\n\x05MySQL\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\x13\n\x0bjdbc_params\x18\x06 \x01(\t\"m\n\x08Postgres\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\x13\n\x0bjdbc_params\x18\x06 \x01(\t\">\n\x02S3\x12\x1d\n\x15\x61ws_secret_access_key\x18\x01 \x01(\t\x12\x19\n\x11\x61ws_access_key_id\x18\x02 \x01(\t\"I\n\x08\x42igquery\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\x18\n\x10\x63redentials_json\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\"\x94\x01\n\tSnowflake\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x11\n\twarehouse\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x13\n\x0bjdbc_params\x18\x07 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\t \x01(\t\"\xbb\x01\n\x05Kafka\x12\x19\n\x11\x62ootstrap_servers\x18\x01 \x01(\t\x12\x19\n\x11security_protocol\x18\x02 \x01(\t\x12\x16\n\x0esasl_mechanism\x18\x03 \x01(\t\x12\x18\n\x10sasl_jaas_config\x18\x04 \x01(\t\x12\x1b\n\x13sasl_plain_username\x18\x05 \x01(\t\x12\x1b\n\x13sasl_plain_password\x18\x06 \x01(\t\x12\x10\n\x08group_id\x18\x07 \x01(\t\"\xbc\x03\n\x08\x45xtTable\x12\x39\n\x0bmysql_table\x18\x01 \x01(\x0b\x32\".fennel.proto.connector.MySQLTableH\x00\x12\x39\n\x08pg_table\x18\x02 \x01(\x0b\x32%.fennel.proto.connector.PostgresTableH\x00\x12\x33\n\x08s3_table\x18\x03 \x01(\x0b\x32\x1f.fennel.proto.connector.S3TableH\x00\x12\x39\n\x0bkafka_topic\x18\x04 \x01(\x0b\x32\".fennel.proto.connector.KafkaTopicH\x00\x12\x41\n\x0fsnowflake_table\x18\x05 \x01(\x0b\x32&.fennel.proto.connector.SnowflakeTableH\x00\x12?\n\x0e\x62igquery_table\x18\x06 \x01(\x0b\x32%.fennel.proto.connector.BigqueryTableH\x00\x12;\n\x08\x65ndpoint\x18\x07 \x01(\x0b\x32\'.fennel.proto.connector.WebhookEndpointH\x00\x42\t\n\x07variant\"Q\n\nMySQLTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"T\n\rPostgresTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"\x82\x01\n\x07S3Table\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x13\n\x0bpath_prefix\x18\x02 \x01(\t\x12\x11\n\tdelimiter\x18\x04 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x05 \x01(\t\x12/\n\x02\x64\x62\x18\x06 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\"L\n\nKafkaTopic\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\r\n\x05topic\x18\x02 \x01(\t\"T\n\rBigqueryTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"U\n\x0eSnowflakeTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"T\n\x0fWebhookEndpoint\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\"\xc1\x01\n\x06Source\x12/\n\x05table\x18\x01 \x01(\x0b\x32 .fennel.proto.connector.ExtTable\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12(\n\x05\x65very\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x06\x63ursor\x18\x04 \x01(\tH\x00\x88\x01\x01\x12+\n\x08lateness\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\n\x07_cursor\"H\n\x04Sink\x12/\n\x05table\x18\x01 \x01(\x0b\x32 .fennel.proto.connector.ExtTable\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'connector_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXTDATABASE._serialized_start=76
  _EXTDATABASE._serialized_end=524
  _REFERENCE._serialized_start=527
  _REFERENCE._serialized_end=698
  _REFERENCE_EXTDBTYPE._serialized_start=601
  _REFERENCE_EXTDBTYPE._serialized_end=698
  _WEBHOOK._serialized_start=700
  _WEBHOOK._serialized_end=723
  _MYSQL._serialized_start=725
  _MYSQL._serialized_end=831
  _POSTGRES._serialized_start=833
  _POSTGRES._serialized_end=942
  _S3._serialized_start=944
  _S3._serialized_end=1006
  _BIGQUERY._serialized_start=1008
  _BIGQUERY._serialized_end=1081
  _SNOWFLAKE._serialized_start=1084
  _SNOWFLAKE._serialized_end=1232
  _KAFKA._serialized_start=1235
  _KAFKA._serialized_end=1422
  _EXTTABLE._serialized_start=1425
  _EXTTABLE._serialized_end=1869
  _MYSQLTABLE._serialized_start=1871
  _MYSQLTABLE._serialized_end=1952
  _POSTGRESTABLE._serialized_start=1954
  _POSTGRESTABLE._serialized_end=2038
  _S3TABLE._serialized_start=2041
  _S3TABLE._serialized_end=2171
  _KAFKATOPIC._serialized_start=2173
  _KAFKATOPIC._serialized_end=2249
  _BIGQUERYTABLE._serialized_start=2251
  _BIGQUERYTABLE._serialized_end=2335
  _SNOWFLAKETABLE._serialized_start=2337
  _SNOWFLAKETABLE._serialized_end=2422
  _WEBHOOKENDPOINT._serialized_start=2424
  _WEBHOOKENDPOINT._serialized_end=2508
  _SOURCE._serialized_start=2511
  _SOURCE._serialized_end=2704
  _SINK._serialized_start=2706
  _SINK._serialized_end=2778
# @@protoc_insertion_point(module_scope)
