"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import window_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PreSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUM_FIELD_NUMBER: builtins.int
    AVERAGE_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    @property
    def sum(self) -> global___Sum: ...
    @property
    def average(self) -> global___Average: ...
    @property
    def count(self) -> global___Count: ...
    def __init__(
        self,
        *,
        sum: global___Sum | None = ...,
        average: global___Average | None = ...,
        count: global___Count | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["average", b"average", "count", b"count", "sum", b"sum", "variant", b"variant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["average", b"average", "count", b"count", "sum", b"sum", "variant", b"variant"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["variant", b"variant"]) -> typing_extensions.Literal["sum", "average", "count"] | None: ...

global___PreSpec = PreSpec

class Sum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OF_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    of: builtins.str
    name: builtins.str
    @property
    def window(self) -> window_pb2.Window: ...
    def __init__(
        self,
        *,
        of: builtins.str = ...,
        name: builtins.str = ...,
        window: window_pb2.Window | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["window", b"window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "of", b"of", "window", b"window"]) -> None: ...

global___Sum = Sum

class Average(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OF_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    DEFAULT_FIELD_NUMBER: builtins.int
    of: builtins.str
    name: builtins.str
    @property
    def window(self) -> window_pb2.Window: ...
    default: builtins.float
    def __init__(
        self,
        *,
        of: builtins.str = ...,
        name: builtins.str = ...,
        window: window_pb2.Window | None = ...,
        default: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["window", b"window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default", b"default", "name", b"name", "of", b"of", "window", b"window"]) -> None: ...

global___Average = Average

class Count(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def window(self) -> window_pb2.Window: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        window: window_pb2.Window | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["window", b"window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "window", b"window"]) -> None: ...

global___Count = Count
