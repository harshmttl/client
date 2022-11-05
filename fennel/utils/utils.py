from __future__ import annotations

import ast
import dataclasses
import datetime
import hashlib
import inspect
import json
import textwrap
from typing import Any
from typing import (Dict, List, Mapping, Tuple, Type,
                    TypeVar, Union)

Tags = Union[List[str], Tuple[str, ...], str]

T = TypeVar('T')


def _json_default(item: Any):
    try:
        return dataclasses.asdict(item)
    except TypeError:
        pass
    if isinstance(item, datetime.datetime):
        return item.isoformat(timespec='microseconds')

    if isinstance(item, bytes):
        return item.hex()

    if callable(item) and not inspect.isclass(item):
        return hashlib.md5(inspect.getsource(item).encode('utf-8')).hexdigest()

    if isinstance(item, datetime.timedelta):
        return str(item.total_seconds())

    raise TypeError(f"object of type {type(item).__name__} not hashable")


def _json_dumps(thing: Any):
    return json.dumps(
        thing,
        default=_json_default,
        ensure_ascii=False,
        sort_keys=True,
        indent=None,
        separators=(',', ':'),
    )


def fhash(*items: Any):
    """Fennel Hash that is used to uniquely identify any python object."""
    items = list(items)
    return hashlib.md5(_json_dumps(items).encode('utf-8')).hexdigest()


def parse_annotation_comments(cls: Type[T]) -> Mapping[str, str]:
    try:
        source = textwrap.dedent(inspect.getsource(cls))

        source_lines = source.splitlines()
        tree = ast.parse(source)
        if len(tree.body) != 1:
            return {}

        comments_for_annotations: Dict[str, str] = {}
        class_def = tree.body[0]
        if isinstance(class_def, ast.ClassDef):
            for stmt in class_def.body:
                if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target,
                        ast.Name):
                    line = stmt.lineno - 2
                    comments: List[str] = []
                    while line >= 0 and source_lines[line].strip().startswith(
                            '#'):
                        comment = source_lines[line].strip().strip('#').strip()
                        comments.insert(0, comment)
                        line -= 1

                    if len(comments) > 0:
                        comments_for_annotations[
                            stmt.target.id] = textwrap.dedent(
                            '\n'.join(comments))

        return comments_for_annotations
    except Exception:
        return {}
