# Verbose, notice, and spam log levels for Python's logging module.
#
# Author: Glenn Matthews <glenn@e-dad.net>
# Last Change: July 26, 2016
# URL: https://verboselogs.readthedocs.io

"""
Pylint_ plugin to fix invalid errors about the :mod:`logging` module.

.. _Pylint: https://pypi.python.org/pypi/pylint
"""

from astroid import MANAGER, scoped_nodes, nodes


def register(linter):
    """No-op (required by Pylint)."""


def verboselogs_class_transform(cls):
    """Make Pylint aware of ``RootLogger.verbose()``, ``RootLogger.notice()``, and ``RootLogger.spam()``."""
    if cls.name == 'RootLogger':
        for meth in ['notice', 'verbose', 'spam']:
            cls.locals[meth] = [scoped_nodes.Function(meth, None)]


def verboselogs_module_transform(mod):
    """Make Pylint aware of ``logging.VERBOSE``, ``logging.notice()``, and ``logging.SPAM``."""
    if mod.name == 'logging':
        for const in ['NOTICE', 'VERBOSE', 'SPAM']:
            mod.locals[const] = [nodes.Const(const)]


# Register the above methods with Pylint.
MANAGER.register_transform(scoped_nodes.Class, verboselogs_class_transform)
MANAGER.register_transform(scoped_nodes.Module, verboselogs_module_transform)
