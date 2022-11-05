from __future__ import annotations

import pyarrow as pa
import types
from datetime import datetime
from typing import (get_args, get_origin, Union)


def get_pyarrow_field(name: str, type_: types) -> pa.lib.Field:
    """Convert a field name and python type to a pa field."""
    # typing.Optional[x] is an alias for typing.Union[x, None]
    if get_origin(type_) is Union and type(None) == get_args(type_)[1]:
        return pa.field(name, get_pyarrow_schema(get_args(type_)[0]),
            nullable=True)
    elif get_origin(type_) is Union:
        x = [get_pyarrow_field(name, t)
             for t in get_args(type_)]
        return pa.union(x, mode='dense')
    return pa.field(name, get_pyarrow_schema(type_), nullable=False)


def get_pyarrow_schema(type_: types) -> pa.lib.Schema:
    """
    Convert a python type to a pa type (
    https://arrow.apache.org/docs/3.0/python/api/datatypes.html ).
    """
    if type_ is None:
        return None
    elif type_ is bool:
        return pa.bool_()
    elif type_ is int:
        return pa.int64()
    elif type_ is float:
        return pa.float64()
    elif type_ is str:
        return pa.string()
    elif type_ is bytes:
        return pa.binary()
    elif type_ is datetime:
        return pa.timestamp('ns')
    elif get_origin(type_) is tuple:
        return pa.struct([get_pyarrow_field(f'f{i}', t) for i, t in
                          enumerate(get_args(type_))])
    elif get_origin(type_) is list:
        return pa.list_(get_pyarrow_schema(get_args(type_)[0]))
    elif get_origin(type_) is set:
        return pa.map_(
            get_pyarrow_schema(get_args(type_)[0]), pa.null())
    elif get_origin(type_) is dict:
        return pa.map_(get_pyarrow_schema(get_args(type_)[0]),
            get_pyarrow_schema(get_args(type_)[1]))
    elif hasattr(type_, '__dataclass_fields__'):
        return pa.struct(
            [(k, get_pyarrow_schema(v.type)) for k, v in
             type_.__dataclass_fields__.items()])
    else:
        raise ValueError(f'Cannot convert type {type_} to pa schema.')