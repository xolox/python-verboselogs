# Verbose, notice, and spam log levels for Python's logging module.
#
# Author: Glenn Matthews <glenn@e-dad.net>
# Last Change: August 7, 2017
# URL: https://verboselogs.readthedocs.io

"""
Pylint_ plugin to fix invalid errors about the :mod:`logging` module.

.. _Pylint: https://pypi.python.org/pypi/pylint
"""

from astroid import MANAGER

try:
    # astroid 2.x
    from astroid import FunctionDef as FunctionDef
    from astroid import Const as Const
    from astroid import ClassDef as ClassDef
    from astroid import Module as Module
except ImportError:
    # astroid 1.x
    from astroid.scoped_nodes import Function as FunctionDef
    from astroid.nodes import Const as Const
    from astroid.scoped_nodes import Class as ClassDef
    from astroid.scoped_nodes import Module as Module


def register(linter):
    """No-op (required by Pylint)."""


def verboselogs_class_transform(cls):
    """Make Pylint aware of our custom logger methods."""
    if cls.name == 'RootLogger':
        for meth in ['notice', 'spam', 'success', 'verbose']:
            cls.locals[meth] = [FunctionDef(meth, None)]


def verboselogs_module_transform(mod):
    """Make Pylint aware of our custom log levels."""
    if mod.name == 'logging':
        for const in ['NOTICE', 'SPAM', 'SUCCESS', 'VERBOSE']:
            mod.locals[const] = [Const(const)]


# Register the above methods with Pylint.
MANAGER.register_transform(ClassDef, verboselogs_class_transform)
MANAGER.register_transform(Module, verboselogs_module_transform)
