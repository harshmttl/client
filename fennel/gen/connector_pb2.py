# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import fennel.gen.kinesis_pb2 as kinesis__pb2
import fennel.gen.schema_registry_pb2 as schema__registry__pb2
import fennel.gen.schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63onnector.proto\x12\x16\x66\x65nnel.proto.connector\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\rkinesis.proto\x1a\x15schema_registry.proto\x1a\x0cschema.proto\"\x8c\x05\n\x0b\x45xtDatabase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x05mysql\x18\x02 \x01(\x0b\x32\x1d.fennel.proto.connector.MySQLH\x00\x12\x34\n\x08postgres\x18\x03 \x01(\x0b\x32 .fennel.proto.connector.PostgresH\x00\x12\x36\n\treference\x18\x04 \x01(\x0b\x32!.fennel.proto.connector.ReferenceH\x00\x12(\n\x02s3\x18\x05 \x01(\x0b\x32\x1a.fennel.proto.connector.S3H\x00\x12\x34\n\x08\x62igquery\x18\x06 \x01(\x0b\x32 .fennel.proto.connector.BigqueryH\x00\x12\x36\n\tsnowflake\x18\x07 \x01(\x0b\x32!.fennel.proto.connector.SnowflakeH\x00\x12.\n\x05kafka\x18\x08 \x01(\x0b\x32\x1d.fennel.proto.connector.KafkaH\x00\x12\x32\n\x07webhook\x18\t \x01(\x0b\x32\x1f.fennel.proto.connector.WebhookH\x00\x12\x32\n\x07kinesis\x18\n \x01(\x0b\x32\x1f.fennel.proto.connector.KinesisH\x00\x12\x34\n\x08redshift\x18\x0b \x01(\x0b\x32 .fennel.proto.connector.RedshiftH\x00\x12.\n\x05mongo\x18\x0c \x01(\x0b\x32\x1d.fennel.proto.connector.MongoH\x00\x12\x30\n\x06pubsub\x18\r \x01(\x0b\x32\x1e.fennel.proto.connector.PubSubH\x00\x42\t\n\x07variant\"M\n\x0cPubSubFormat\x12\x32\n\x04json\x18\x01 \x01(\x0b\x32\".fennel.proto.connector.JsonFormatH\x00\x42\t\n\x07variant\"\x80\x01\n\x0bKafkaFormat\x12\x32\n\x04json\x18\x01 \x01(\x0b\x32\".fennel.proto.connector.JsonFormatH\x00\x12\x32\n\x04\x61vro\x18\x02 \x01(\x0b\x32\".fennel.proto.connector.AvroFormatH\x00\x42\t\n\x07variant\"\x0c\n\nJsonFormat\"S\n\nAvroFormat\x12\x45\n\x0fschema_registry\x18\x01 \x01(\x0b\x32,.fennel.proto.schema_registry.SchemaRegistry\"\xde\x01\n\tReference\x12;\n\x06\x64\x62type\x18\x01 \x01(\x0e\x32+.fennel.proto.connector.Reference.ExtDBType\"\x93\x01\n\tExtDBType\x12\t\n\x05MYSQL\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\x06\n\x02S3\x10\x02\x12\t\n\x05KAFKA\x10\x03\x12\x0c\n\x08\x42IGQUERY\x10\x04\x12\r\n\tSNOWFLAKE\x10\x05\x12\x0b\n\x07WEBHOOK\x10\x06\x12\x0b\n\x07KINESIS\x10\x07\x12\x0c\n\x08REDSHIFT\x10\x08\x12\t\n\x05MONGO\x10\t\x12\n\n\x06PUBSUB\x10\n\"E\n\x07Webhook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\tretention\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"j\n\x05MySQL\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\x13\n\x0bjdbc_params\x18\x06 \x01(\t\"m\n\x08Postgres\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\x13\n\x0bjdbc_params\x18\x06 \x01(\t\"b\n\x02S3\x12\x1d\n\x15\x61ws_secret_access_key\x18\x01 \x01(\t\x12\x19\n\x11\x61ws_access_key_id\x18\x02 \x01(\t\x12\x15\n\x08role_arn\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_role_arn\"O\n\x08\x42igquery\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x1b\n\x13service_account_key\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\"\x7f\n\tSnowflake\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x11\n\twarehouse\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x07 \x01(\t\"\xfd\x01\n\x05Kafka\x12\x19\n\x11\x62ootstrap_servers\x18\x01 \x01(\t\x12\x19\n\x11security_protocol\x18\x02 \x01(\t\x12\x16\n\x0esasl_mechanism\x18\x03 \x01(\t\x12\x1c\n\x10sasl_jaas_config\x18\x04 \x01(\tB\x02\x18\x01\x12 \n\x13sasl_plain_username\x18\x05 \x01(\tH\x00\x88\x01\x01\x12 \n\x13sasl_plain_password\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x08group_id\x18\x07 \x01(\tB\x02\x18\x01\x42\x16\n\x14_sasl_plain_usernameB\x16\n\x14_sasl_plain_password\"\x1b\n\x07Kinesis\x12\x10\n\x08role_arn\x18\x01 \x01(\t\"d\n\x08Redshift\x12\x1a\n\x12s3_access_role_arn\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\x12\x0e\n\x06schema\x18\x05 \x01(\t\"G\n\x05Mongo\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"9\n\x06PubSub\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x1b\n\x13service_account_key\x18\x02 \x01(\t\"\xc0\x05\n\x08\x45xtTable\x12\x39\n\x0bmysql_table\x18\x01 \x01(\x0b\x32\".fennel.proto.connector.MySQLTableH\x00\x12\x39\n\x08pg_table\x18\x02 \x01(\x0b\x32%.fennel.proto.connector.PostgresTableH\x00\x12\x33\n\x08s3_table\x18\x03 \x01(\x0b\x32\x1f.fennel.proto.connector.S3TableH\x00\x12\x39\n\x0bkafka_topic\x18\x04 \x01(\x0b\x32\".fennel.proto.connector.KafkaTopicH\x00\x12\x41\n\x0fsnowflake_table\x18\x05 \x01(\x0b\x32&.fennel.proto.connector.SnowflakeTableH\x00\x12?\n\x0e\x62igquery_table\x18\x06 \x01(\x0b\x32%.fennel.proto.connector.BigqueryTableH\x00\x12;\n\x08\x65ndpoint\x18\x07 \x01(\x0b\x32\'.fennel.proto.connector.WebhookEndpointH\x00\x12?\n\x0ekinesis_stream\x18\x08 \x01(\x0b\x32%.fennel.proto.connector.KinesisStreamH\x00\x12?\n\x0eredshift_table\x18\t \x01(\x0b\x32%.fennel.proto.connector.RedshiftTableH\x00\x12\x43\n\x10mongo_collection\x18\n \x01(\x0b\x32\'.fennel.proto.connector.MongoCollectionH\x00\x12;\n\x0cpubsub_topic\x18\x0b \x01(\x0b\x32#.fennel.proto.connector.PubSubTopicH\x00\x42\t\n\x07variant\"Q\n\nMySQLTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"z\n\rPostgresTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x16\n\tslot_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0c\n\n_slot_name\"\xf7\x01\n\x07S3Table\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x13\n\x0bpath_prefix\x18\x02 \x01(\t\x12\x11\n\tdelimiter\x18\x04 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x05 \x01(\t\x12/\n\x02\x64\x62\x18\x06 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\npre_sorted\x18\x07 \x01(\x08\x12\x13\n\x0bpath_suffix\x18\x08 \x01(\t\x12.\n\x06spread\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x88\x01\x01\x12\x0f\n\x07headers\x18\t \x03(\tB\t\n\x07_spread\"\x81\x01\n\nKafkaTopic\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x33\n\x06\x66ormat\x18\x03 \x01(\x0b\x32#.fennel.proto.connector.KafkaFormat\"T\n\rBigqueryTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"U\n\x0eSnowflakeTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"\x81\x01\n\x0fWebhookEndpoint\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\x12+\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xd3\x01\n\rKinesisStream\x12\x12\n\nstream_arn\x18\x01 \x01(\t\x12\x39\n\rinit_position\x18\x02 \x01(\x0e\x32\".fennel.proto.kinesis.InitPosition\x12\x32\n\x0einit_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ormat\x18\x04 \x01(\t\x12/\n\x02\x64\x62\x18\x05 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\"T\n\rRedshiftTable\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x12\n\ntable_name\x18\x02 \x01(\t\"\x86\x01\n\x0bPubSubTopic\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x10\n\x08topic_id\x18\x02 \x01(\t\x12\x34\n\x06\x66ormat\x18\x03 \x01(\x0b\x32$.fennel.proto.connector.PubSubFormat\"U\n\x0cPreProcValue\x12\r\n\x03ref\x18\x01 \x01(\tH\x00\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1a.fennel.proto.schema.ValueH\x00\x42\t\n\x07variant\"[\n\x0fMongoCollection\x12/\n\x02\x64\x62\x18\x01 \x01(\x0b\x32#.fennel.proto.connector.ExtDatabase\x12\x17\n\x0f\x63ollection_name\x18\x02 \x01(\t\"\xf4\x04\n\x06Source\x12/\n\x05table\x18\x01 \x01(\x0b\x32 .fennel.proto.connector.ExtTable\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\x12\n\nds_version\x18\x03 \x01(\r\x12(\n\x05\x65very\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x06\x63ursor\x18\x05 \x01(\tH\x00\x88\x01\x01\x12+\n\x08\x64isorder\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x17\n\x0ftimestamp_field\x18\x07 \x01(\t\x12\x30\n\x03\x63\x64\x63\x18\x08 \x01(\x0e\x32#.fennel.proto.connector.CDCStrategy\x12\x31\n\rstarting_from\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12=\n\x08pre_proc\x18\n \x03(\x0b\x32+.fennel.proto.connector.Source.PreProcEntry\x12\x0f\n\x07version\x18\x0b \x01(\r\x12\x0f\n\x07\x62ounded\x18\x0c \x01(\x08\x12\x30\n\x08idleness\x18\r \x01(\x0b\x32\x19.google.protobuf.DurationH\x01\x88\x01\x01\x12)\n\x05until\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aT\n\x0cPreProcEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.fennel.proto.connector.PreProcValue:\x02\x38\x01\x42\t\n\x07_cursorB\x0b\n\t_idleness\"\x8e\x01\n\x04Sink\x12/\n\x05table\x18\x01 \x01(\x0b\x32 .fennel.proto.connector.ExtTable\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\x12\n\nds_version\x18\x03 \x01(\r\x12\x30\n\x03\x63\x64\x63\x18\x04 \x01(\x0e\x32#.fennel.proto.connector.CDCStrategy*K\n\x0b\x43\x44\x43Strategy\x12\n\n\x06\x41ppend\x10\x00\x12\n\n\x06Upsert\x10\x01\x12\x0c\n\x08\x44\x65\x62\x65zium\x10\x02\x12\n\n\x06Native\x10\x03\x12\n\n\x06\x44\x65lete\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'connector_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_KAFKA'].fields_by_name['sasl_jaas_config']._options = None
  _globals['_KAFKA'].fields_by_name['sasl_jaas_config']._serialized_options = b'\030\001'
  _globals['_KAFKA'].fields_by_name['group_id']._options = None
  _globals['_KAFKA'].fields_by_name['group_id']._serialized_options = b'\030\001'
  _globals['_SOURCE_PREPROCENTRY']._options = None
  _globals['_SOURCE_PREPROCENTRY']._serialized_options = b'8\001'
  _globals['_CDCSTRATEGY']._serialized_start=5462
  _globals['_CDCSTRATEGY']._serialized_end=5537
  _globals['_EXTDATABASE']._serialized_start=161
  _globals['_EXTDATABASE']._serialized_end=813
  _globals['_PUBSUBFORMAT']._serialized_start=815
  _globals['_PUBSUBFORMAT']._serialized_end=892
  _globals['_KAFKAFORMAT']._serialized_start=895
  _globals['_KAFKAFORMAT']._serialized_end=1023
  _globals['_JSONFORMAT']._serialized_start=1025
  _globals['_JSONFORMAT']._serialized_end=1037
  _globals['_AVROFORMAT']._serialized_start=1039
  _globals['_AVROFORMAT']._serialized_end=1122
  _globals['_REFERENCE']._serialized_start=1125
  _globals['_REFERENCE']._serialized_end=1347
  _globals['_REFERENCE_EXTDBTYPE']._serialized_start=1200
  _globals['_REFERENCE_EXTDBTYPE']._serialized_end=1347
  _globals['_WEBHOOK']._serialized_start=1349
  _globals['_WEBHOOK']._serialized_end=1418
  _globals['_MYSQL']._serialized_start=1420
  _globals['_MYSQL']._serialized_end=1526
  _globals['_POSTGRES']._serialized_start=1528
  _globals['_POSTGRES']._serialized_end=1637
  _globals['_S3']._serialized_start=1639
  _globals['_S3']._serialized_end=1737
  _globals['_BIGQUERY']._serialized_start=1739
  _globals['_BIGQUERY']._serialized_end=1818
  _globals['_SNOWFLAKE']._serialized_start=1820
  _globals['_SNOWFLAKE']._serialized_end=1947
  _globals['_KAFKA']._serialized_start=1950
  _globals['_KAFKA']._serialized_end=2203
  _globals['_KINESIS']._serialized_start=2205
  _globals['_KINESIS']._serialized_end=2232
  _globals['_REDSHIFT']._serialized_start=2234
  _globals['_REDSHIFT']._serialized_end=2334
  _globals['_MONGO']._serialized_start=2336
  _globals['_MONGO']._serialized_end=2407
  _globals['_PUBSUB']._serialized_start=2409
  _globals['_PUBSUB']._serialized_end=2466
  _globals['_EXTTABLE']._serialized_start=2469
  _globals['_EXTTABLE']._serialized_end=3173
  _globals['_MYSQLTABLE']._serialized_start=3175
  _globals['_MYSQLTABLE']._serialized_end=3256
  _globals['_POSTGRESTABLE']._serialized_start=3258
  _globals['_POSTGRESTABLE']._serialized_end=3380
  _globals['_S3TABLE']._serialized_start=3383
  _globals['_S3TABLE']._serialized_end=3630
  _globals['_KAFKATOPIC']._serialized_start=3633
  _globals['_KAFKATOPIC']._serialized_end=3762
  _globals['_BIGQUERYTABLE']._serialized_start=3764
  _globals['_BIGQUERYTABLE']._serialized_end=3848
  _globals['_SNOWFLAKETABLE']._serialized_start=3850
  _globals['_SNOWFLAKETABLE']._serialized_end=3935
  _globals['_WEBHOOKENDPOINT']._serialized_start=3938
  _globals['_WEBHOOKENDPOINT']._serialized_end=4067
  _globals['_KINESISSTREAM']._serialized_start=4070
  _globals['_KINESISSTREAM']._serialized_end=4281
  _globals['_REDSHIFTTABLE']._serialized_start=4283
  _globals['_REDSHIFTTABLE']._serialized_end=4367
  _globals['_PUBSUBTOPIC']._serialized_start=4370
  _globals['_PUBSUBTOPIC']._serialized_end=4504
  _globals['_PREPROCVALUE']._serialized_start=4506
  _globals['_PREPROCVALUE']._serialized_end=4591
  _globals['_MONGOCOLLECTION']._serialized_start=4593
  _globals['_MONGOCOLLECTION']._serialized_end=4684
  _globals['_SOURCE']._serialized_start=4687
  _globals['_SOURCE']._serialized_end=5315
  _globals['_SOURCE_PREPROCENTRY']._serialized_start=5207
  _globals['_SOURCE_PREPROCENTRY']._serialized_end=5291
  _globals['_SINK']._serialized_start=5318
  _globals['_SINK']._serialized_end=5460
# @@protoc_insertion_point(module_scope)
