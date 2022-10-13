# coding: utf-8

import ast
import glob
import importlib
import inspect
import sys
import textwrap

from cognitive_complexity.api import get_cognitive_complexity


def get_top_level_names(module):
    for name in dir(module):
        if inspect.getmodule(func := getattr(module, name)) == module and (
            inspect.isclass(func) or inspect.isfunction(func)
        ):
            yield func


def get_methods(klass):
    for name in dir(klass):
        if inspect.isfunction(
            method := getattr(klass, name)
        ) and method.__qualname__.startswith(klass.__qualname__):
            yield method


def get_cc(obj):
    return get_cognitive_complexity(
        ast.parse(textwrap.dedent(inspect.getsource(obj))).body[0]
    )


if __name__ == "__main__":
    for module_name in [
        fn[:-3].replace("/", ".")
        for fn in sum([glob.glob(arg) for arg in sys.argv[1:]], [])
    ]:
        print(f"{module_name}")
        for member in get_top_level_names(importlib.import_module(module_name)):
            print(
                f"\t{'C' if inspect.isclass(member) else 'F'} {member.__name__} {get_cc(member)}"
            )
            if inspect.isclass(member):
                for method in get_methods(member):
                    print(f"\tM {member.__name__}.{method.__name__} {get_cc(method)}")
