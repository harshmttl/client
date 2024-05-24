"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import metadata_pb2
import pycode_pb2
import schema_pb2
import spec_pb2
import sys
import typing
import window_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CoreDataset(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class FieldMetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> metadata_pb2.Metadata: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: metadata_pb2.Metadata | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    DSSCHEMA_FIELD_NUMBER: builtins.int
    HISTORY_FIELD_NUMBER: builtins.int
    RETENTION_FIELD_NUMBER: builtins.int
    FIELD_METADATA_FIELD_NUMBER: builtins.int
    PYCODE_FIELD_NUMBER: builtins.int
    IS_SOURCE_DATASET_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def metadata(self) -> metadata_pb2.Metadata: ...
    @property
    def dsschema(self) -> schema_pb2.DSSchema: ...
    @property
    def history(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def retention(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def field_metadata(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, metadata_pb2.Metadata]: ...
    @property
    def pycode(self) -> pycode_pb2.PyCode: ...
    is_source_dataset: builtins.bool
    version: builtins.int
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Union of all tags based on ownership and dataflow semantics."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        metadata: metadata_pb2.Metadata | None = ...,
        dsschema: schema_pb2.DSSchema | None = ...,
        history: google.protobuf.duration_pb2.Duration | None = ...,
        retention: google.protobuf.duration_pb2.Duration | None = ...,
        field_metadata: collections.abc.Mapping[builtins.str, metadata_pb2.Metadata] | None = ...,
        pycode: pycode_pb2.PyCode | None = ...,
        is_source_dataset: builtins.bool = ...,
        version: builtins.int = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dsschema", b"dsschema", "history", b"history", "metadata", b"metadata", "pycode", b"pycode", "retention", b"retention"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dsschema", b"dsschema", "field_metadata", b"field_metadata", "history", b"history", "is_source_dataset", b"is_source_dataset", "metadata", b"metadata", "name", b"name", "pycode", b"pycode", "retention", b"retention", "tags", b"tags", "version", b"version"]) -> None: ...

global___CoreDataset = CoreDataset

@typing_extensions.final
class OnDemand(google.protobuf.message.Message):
    """All integers representing time are in microseconds and hence should be int64."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_SOURCE_CODE_FIELD_NUMBER: builtins.int
    FUNCTION_FIELD_NUMBER: builtins.int
    EXPIRES_AFTER_FIELD_NUMBER: builtins.int
    function_source_code: builtins.str
    function: builtins.bytes
    expires_after: builtins.int
    """TODO(mohit): Make this duration"""
    def __init__(
        self,
        *,
        function_source_code: builtins.str = ...,
        function: builtins.bytes = ...,
        expires_after: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expires_after", b"expires_after", "function", b"function", "function_source_code", b"function_source_code"]) -> None: ...

global___OnDemand = OnDemand

@typing_extensions.final
class Pipeline(google.protobuf.message.Message):
    """----------------------------------------------------------------------------------------------
    Pipeline
    ----------------------------------------------------------------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DATASET_NAME_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    INPUT_DATASET_NAMES_FIELD_NUMBER: builtins.int
    DS_VERSION_FIELD_NUMBER: builtins.int
    PYCODE_FIELD_NUMBER: builtins.int
    name: builtins.str
    dataset_name: builtins.str
    signature: builtins.str
    @property
    def metadata(self) -> metadata_pb2.Metadata: ...
    @property
    def input_dataset_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    ds_version: builtins.int
    @property
    def pycode(self) -> pycode_pb2.PyCode: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        dataset_name: builtins.str = ...,
        signature: builtins.str = ...,
        metadata: metadata_pb2.Metadata | None = ...,
        input_dataset_names: collections.abc.Iterable[builtins.str] | None = ...,
        ds_version: builtins.int = ...,
        pycode: pycode_pb2.PyCode | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "pycode", b"pycode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_name", b"dataset_name", "ds_version", b"ds_version", "input_dataset_names", b"input_dataset_names", "metadata", b"metadata", "name", b"name", "pycode", b"pycode", "signature", b"signature"]) -> None: ...

global___Pipeline = Pipeline

@typing_extensions.final
class Operator(google.protobuf.message.Message):
    """Each operator corresponds to a valid operation as part of a pipeline"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    IS_ROOT_FIELD_NUMBER: builtins.int
    PIPELINE_NAME_FIELD_NUMBER: builtins.int
    DATASET_NAME_FIELD_NUMBER: builtins.int
    DS_VERSION_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    JOIN_FIELD_NUMBER: builtins.int
    TRANSFORM_FIELD_NUMBER: builtins.int
    UNION_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    DATASET_REF_FIELD_NUMBER: builtins.int
    RENAME_FIELD_NUMBER: builtins.int
    DROP_FIELD_NUMBER: builtins.int
    EXPLODE_FIELD_NUMBER: builtins.int
    DEDUP_FIELD_NUMBER: builtins.int
    FIRST_FIELD_NUMBER: builtins.int
    ASSIGN_FIELD_NUMBER: builtins.int
    DROPNULL_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    LATEST_FIELD_NUMBER: builtins.int
    CHANGELOG_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Every operator has an ID assigned by the client"""
    is_root: builtins.bool
    """If the operator is the "root" operator in the given `pipeline` of the given
    `dataset`.
    """
    pipeline_name: builtins.str
    """Name of the pipeline in which this operator is defined in"""
    dataset_name: builtins.str
    """Name of the dataset in which the pipeline is defined in"""
    ds_version: builtins.int
    @property
    def aggregate(self) -> global___Aggregate: ...
    @property
    def join(self) -> global___Join: ...
    @property
    def transform(self) -> global___Transform: ...
    @property
    def union(self) -> global___Union: ...
    @property
    def filter(self) -> global___Filter: ...
    @property
    def dataset_ref(self) -> global___DatasetRef: ...
    @property
    def rename(self) -> global___Rename: ...
    @property
    def drop(self) -> global___Drop: ...
    @property
    def explode(self) -> global___Explode: ...
    @property
    def dedup(self) -> global___Dedup: ...
    @property
    def first(self) -> global___First: ...
    @property
    def assign(self) -> global___Assign: ...
    @property
    def dropnull(self) -> global___Dropnull: ...
    @property
    def window(self) -> global___WindowOperatorKind: ...
    @property
    def latest(self) -> global___Latest: ...
    @property
    def changelog(self) -> global___Changelog: ...
    name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT

    Name of the operator assigned by the server
    """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        is_root: builtins.bool = ...,
        pipeline_name: builtins.str = ...,
        dataset_name: builtins.str = ...,
        ds_version: builtins.int = ...,
        aggregate: global___Aggregate | None = ...,
        join: global___Join | None = ...,
        transform: global___Transform | None = ...,
        union: global___Union | None = ...,
        filter: global___Filter | None = ...,
        dataset_ref: global___DatasetRef | None = ...,
        rename: global___Rename | None = ...,
        drop: global___Drop | None = ...,
        explode: global___Explode | None = ...,
        dedup: global___Dedup | None = ...,
        first: global___First | None = ...,
        assign: global___Assign | None = ...,
        dropnull: global___Dropnull | None = ...,
        window: global___WindowOperatorKind | None = ...,
        latest: global___Latest | None = ...,
        changelog: global___Changelog | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aggregate", b"aggregate", "assign", b"assign", "changelog", b"changelog", "dataset_ref", b"dataset_ref", "dedup", b"dedup", "drop", b"drop", "dropnull", b"dropnull", "explode", b"explode", "filter", b"filter", "first", b"first", "join", b"join", "kind", b"kind", "latest", b"latest", "rename", b"rename", "transform", b"transform", "union", b"union", "window", b"window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate", b"aggregate", "assign", b"assign", "changelog", b"changelog", "dataset_name", b"dataset_name", "dataset_ref", b"dataset_ref", "dedup", b"dedup", "drop", b"drop", "dropnull", b"dropnull", "ds_version", b"ds_version", "explode", b"explode", "filter", b"filter", "first", b"first", "id", b"id", "is_root", b"is_root", "join", b"join", "kind", b"kind", "latest", b"latest", "name", b"name", "pipeline_name", b"pipeline_name", "rename", b"rename", "transform", b"transform", "union", b"union", "window", b"window"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind", b"kind"]) -> typing_extensions.Literal["aggregate", "join", "transform", "union", "filter", "dataset_ref", "rename", "drop", "explode", "dedup", "first", "assign", "dropnull", "window", "latest", "changelog"] | None: ...

global___Operator = Operator

@typing_extensions.final
class Aggregate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    SPECS_FIELD_NUMBER: builtins.int
    ALONG_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[spec_pb2.PreSpec]: ...
    along: builtins.str
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        specs: collections.abc.Iterable[spec_pb2.PreSpec] | None = ...,
        along: builtins.str | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_along", b"_along", "along", b"along"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_along", b"_along", "along", b"along", "keys", b"keys", "operand_id", b"operand_id", "operand_name", b"operand_name", "specs", b"specs"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_along", b"_along"]) -> typing_extensions.Literal["along"] | None: ...

global___Aggregate = Aggregate

@typing_extensions.final
class Join(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _How:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HowEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Join._How.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Left: Join._How.ValueType  # 0
        Inner: Join._How.ValueType  # 1

    class How(_How, metaclass=_HowEnumTypeWrapper): ...
    Left: Join.How.ValueType  # 0
    Inner: Join.How.ValueType  # 1

    @typing_extensions.final
    class OnEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    LHS_OPERAND_ID_FIELD_NUMBER: builtins.int
    RHS_DSREF_OPERAND_ID_FIELD_NUMBER: builtins.int
    ON_FIELD_NUMBER: builtins.int
    WITHIN_LOW_FIELD_NUMBER: builtins.int
    WITHIN_HIGH_FIELD_NUMBER: builtins.int
    LHS_OPERAND_NAME_FIELD_NUMBER: builtins.int
    RHS_DSREF_OPERAND_NAME_FIELD_NUMBER: builtins.int
    HOW_FIELD_NUMBER: builtins.int
    lhs_operand_id: builtins.str
    rhs_dsref_operand_id: builtins.str
    """RHS of a JOIN can only be a dataset, here it refers to the DSRef operator"""
    @property
    def on(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Map of left field name to right field name to join on."""
    @property
    def within_low(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def within_high(self) -> google.protobuf.duration_pb2.Duration: ...
    lhs_operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    rhs_dsref_operand_name: builtins.str
    how: global___Join.How.ValueType
    def __init__(
        self,
        *,
        lhs_operand_id: builtins.str = ...,
        rhs_dsref_operand_id: builtins.str = ...,
        on: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        within_low: google.protobuf.duration_pb2.Duration | None = ...,
        within_high: google.protobuf.duration_pb2.Duration | None = ...,
        lhs_operand_name: builtins.str = ...,
        rhs_dsref_operand_name: builtins.str = ...,
        how: global___Join.How.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_within_high", b"_within_high", "_within_low", b"_within_low", "within_high", b"within_high", "within_low", b"within_low"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_within_high", b"_within_high", "_within_low", b"_within_low", "how", b"how", "lhs_operand_id", b"lhs_operand_id", "lhs_operand_name", b"lhs_operand_name", "on", b"on", "rhs_dsref_operand_id", b"rhs_dsref_operand_id", "rhs_dsref_operand_name", b"rhs_dsref_operand_name", "within_high", b"within_high", "within_low", b"within_low"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_within_high", b"_within_high"]) -> typing_extensions.Literal["within_high"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_within_low", b"_within_low"]) -> typing_extensions.Literal["within_low"] | None: ...

global___Join = Join

@typing_extensions.final
class Transform(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SchemaEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> schema_pb2.DataType: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: schema_pb2.DataType | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    OPERAND_ID_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    PYCODE_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def schema(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, schema_pb2.DataType]: ...
    @property
    def pycode(self) -> pycode_pb2.PyCode: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        schema: collections.abc.Mapping[builtins.str, schema_pb2.DataType] | None = ...,
        pycode: pycode_pb2.PyCode | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pycode", b"pycode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["operand_id", b"operand_id", "operand_name", b"operand_name", "pycode", b"pycode", "schema", b"schema"]) -> None: ...

global___Transform = Transform

@typing_extensions.final
class Filter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    PYCODE_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def pycode(self) -> pycode_pb2.PyCode: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        pycode: pycode_pb2.PyCode | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pycode", b"pycode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["operand_id", b"operand_id", "operand_name", b"operand_name", "pycode", b"pycode"]) -> None: ...

global___Filter = Filter

@typing_extensions.final
class Assign(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    PYCODE_FIELD_NUMBER: builtins.int
    COLUMN_NAME_FIELD_NUMBER: builtins.int
    OUTPUT_TYPE_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def pycode(self) -> pycode_pb2.PyCode: ...
    column_name: builtins.str
    @property
    def output_type(self) -> schema_pb2.DataType: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        pycode: pycode_pb2.PyCode | None = ...,
        column_name: builtins.str = ...,
        output_type: schema_pb2.DataType | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["output_type", b"output_type", "pycode", b"pycode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["column_name", b"column_name", "operand_id", b"operand_id", "operand_name", b"operand_name", "output_type", b"output_type", "pycode", b"pycode"]) -> None: ...

global___Assign = Assign

@typing_extensions.final
class Dropnull(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        columns: collections.abc.Iterable[builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["columns", b"columns", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Dropnull = Dropnull

@typing_extensions.final
class Drop(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    DROPCOLS_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def dropcols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        dropcols: collections.abc.Iterable[builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dropcols", b"dropcols", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Drop = Drop

@typing_extensions.final
class Rename(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ColumnMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    OPERAND_ID_FIELD_NUMBER: builtins.int
    COLUMN_MAP_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def column_map(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        column_map: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["column_map", b"column_map", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Rename = Rename

@typing_extensions.final
class Union(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_IDS_FIELD_NUMBER: builtins.int
    OPERAND_NAMES_FIELD_NUMBER: builtins.int
    @property
    def operand_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def operand_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
        THE CLIENT
        """
    def __init__(
        self,
        *,
        operand_ids: collections.abc.Iterable[builtins.str] | None = ...,
        operand_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["operand_ids", b"operand_ids", "operand_names", b"operand_names"]) -> None: ...

global___Union = Union

@typing_extensions.final
class Dedup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        columns: collections.abc.Iterable[builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["columns", b"columns", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Dedup = Dedup

@typing_extensions.final
class Explode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        columns: collections.abc.Iterable[builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["columns", b"columns", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Explode = Explode

@typing_extensions.final
class First(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    BY_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def by(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        by: collections.abc.Iterable[builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["by", b"by", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___First = First

@typing_extensions.final
class Latest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    BY_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def by(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        by: collections.abc.Iterable[builtins.str] | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["by", b"by", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Latest = Latest

@typing_extensions.final
class Changelog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    DELETE_COLUMN_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    delete_column: builtins.str
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        delete_column: builtins.str = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_column", b"delete_column", "operand_id", b"operand_id", "operand_name", b"operand_name"]) -> None: ...

global___Changelog = Changelog

@typing_extensions.final
class WindowOperatorKind(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_ID_FIELD_NUMBER: builtins.int
    WINDOW_TYPE_FIELD_NUMBER: builtins.int
    BY_FIELD_NUMBER: builtins.int
    FIELD_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    OPERAND_NAME_FIELD_NUMBER: builtins.int
    operand_id: builtins.str
    @property
    def window_type(self) -> window_pb2.Window: ...
    @property
    def by(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    field: builtins.str
    @property
    def summary(self) -> window_pb2.Summary: ...
    operand_name: builtins.str
    """NOTE: FOLLOWING PROPERTIES ARE SET BY THE SERVER AND WILL BE IGNORED BY
    THE CLIENT
    """
    def __init__(
        self,
        *,
        operand_id: builtins.str = ...,
        window_type: window_pb2.Window | None = ...,
        by: collections.abc.Iterable[builtins.str] | None = ...,
        field: builtins.str = ...,
        summary: window_pb2.Summary | None = ...,
        operand_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_summary", b"_summary", "summary", b"summary", "window_type", b"window_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_summary", b"_summary", "by", b"by", "field", b"field", "operand_id", b"operand_id", "operand_name", b"operand_name", "summary", b"summary", "window_type", b"window_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_summary", b"_summary"]) -> typing_extensions.Literal["summary"] | None: ...

global___WindowOperatorKind = WindowOperatorKind

@typing_extensions.final
class DatasetRef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REFERRING_DATASET_NAME_FIELD_NUMBER: builtins.int
    referring_dataset_name: builtins.str
    def __init__(
        self,
        *,
        referring_dataset_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["referring_dataset_name", b"referring_dataset_name"]) -> None: ...

global___DatasetRef = DatasetRef

@typing_extensions.final
class Dataflow(google.protobuf.message.Message):
    """----------------------------------------------------------------------------------------------
    Lineage
    ----------------------------------------------------------------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PipelineDataflow(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DATASET_NAME_FIELD_NUMBER: builtins.int
        PIPELINE_NAME_FIELD_NUMBER: builtins.int
        INPUT_DATAFLOWS_FIELD_NUMBER: builtins.int
        dataset_name: builtins.str
        pipeline_name: builtins.str
        @property
        def input_dataflows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Dataflow]: ...
        def __init__(
            self,
            *,
            dataset_name: builtins.str = ...,
            pipeline_name: builtins.str = ...,
            input_dataflows: collections.abc.Iterable[global___Dataflow] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["dataset_name", b"dataset_name", "input_dataflows", b"input_dataflows", "pipeline_name", b"pipeline_name"]) -> None: ...

    DATASET_NAME_FIELD_NUMBER: builtins.int
    PIPELINE_DATAFLOW_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    dataset_name: builtins.str
    @property
    def pipeline_dataflow(self) -> global___Dataflow.PipelineDataflow: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        dataset_name: builtins.str = ...,
        pipeline_dataflow: global___Dataflow.PipelineDataflow | None = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset_name", b"dataset_name", "kind", b"kind", "pipeline_dataflow", b"pipeline_dataflow"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_name", b"dataset_name", "kind", b"kind", "pipeline_dataflow", b"pipeline_dataflow", "tags", b"tags"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind", b"kind"]) -> typing_extensions.Literal["dataset_name", "pipeline_dataflow"] | None: ...

global___Dataflow = Dataflow

@typing_extensions.final
class PipelineLineages(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_NAME_FIELD_NUMBER: builtins.int
    PIPELINE_NAME_FIELD_NUMBER: builtins.int
    INPUT_DATASETS_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    dataset_name: builtins.str
    pipeline_name: builtins.str
    @property
    def input_datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DatasetLineages]: ...
    active: builtins.bool
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        dataset_name: builtins.str = ...,
        pipeline_name: builtins.str = ...,
        input_datasets: collections.abc.Iterable[global___DatasetLineages] | None = ...,
        active: builtins.bool = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["active", b"active", "dataset_name", b"dataset_name", "input_datasets", b"input_datasets", "pipeline_name", b"pipeline_name", "tags", b"tags"]) -> None: ...

global___PipelineLineages = PipelineLineages

@typing_extensions.final
class DatasetPipelineLineages(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIPELINE_LINEAGES_FIELD_NUMBER: builtins.int
    @property
    def pipeline_lineages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelineLineages]: ...
    def __init__(
        self,
        *,
        pipeline_lineages: collections.abc.Iterable[global___PipelineLineages] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pipeline_lineages", b"pipeline_lineages"]) -> None: ...

global___DatasetPipelineLineages = DatasetPipelineLineages

@typing_extensions.final
class DatasetLineages(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_DATASET_FIELD_NUMBER: builtins.int
    DERIVED_DATASET_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    source_dataset: builtins.str
    """If it is a source dataset, it will have a source dataset name."""
    @property
    def derived_dataset(self) -> global___DatasetPipelineLineages:
        """If it is a derived dataset, it will have pipeline lineages, one for each
        pipeline in the dataset.
        """
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        source_dataset: builtins.str = ...,
        derived_dataset: global___DatasetPipelineLineages | None = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["derived_dataset", b"derived_dataset", "kind", b"kind", "source_dataset", b"source_dataset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["derived_dataset", b"derived_dataset", "kind", b"kind", "source_dataset", b"source_dataset", "tags", b"tags"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind", b"kind"]) -> typing_extensions.Literal["source_dataset", "derived_dataset"] | None: ...

global___DatasetLineages = DatasetLineages
