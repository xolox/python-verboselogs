"""
Pylint plugin to fix invalid errors about the logging module.

Author: Glenn Matthews <glenn@e-dad.net>
Last Change: June 22, 2016
URL: https://pypi.python.org/pypi/verboselogs
"""

from astroid import MANAGER, scoped_nodes, nodes


def register(linter):
    """No-op (required by Pylint)."""
    pass


def verboselogs_class_transform(cls):
    """Make Pylint aware of RootLogger.verbose and RootLogger.spam."""
    if cls.name == 'RootLogger':
        for meth in ['verbose', 'spam']:
            cls.locals[meth] = [scoped_nodes.Function(meth, None)]


def verboselogs_module_transform(mod):
    """Make Pylint aware of logging.VERBOSE and logging.SPAM."""
    if mod.name == 'logging':
        for const in ['VERBOSE', 'SPAM']:
            mod.locals[const] = [nodes.Const(const)]

# Register the above methods with Pylint.
MANAGER.register_transform(scoped_nodes.Class, verboselogs_class_transform)
MANAGER.register_transform(scoped_nodes.Module, verboselogs_module_transform)
