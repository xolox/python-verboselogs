# Verbose, notice, and spam log levels for Python's logging module.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: July 26, 2016
# URL: https://verboselogs.readthedocs.io

"""Test suite for the `verboselogs` package."""

# Standard library modules.
import logging
import random
import string
import sys
import unittest

# Modules included in our package.
import verboselogs

# Test dependencies.
import coloredlogs
import mock


class VerboseLogsTestCase(unittest.TestCase):

    """Container for the `verboselogs` tests."""

    def setUp(self):
        """Enable logging to the terminal."""
        coloredlogs.install(level='DEBUG')

    def test_install(self):
        """Test the :func:`verboselogs.install()` function."""
        default_logger = logging.getLogger(random_string())
        assert isinstance(default_logger, logging.Logger)
        verboselogs.install()
        custom_logger = logging.getLogger(random_string())
        assert isinstance(custom_logger, verboselogs.VerboseLogger)

    def test_custom_methods(self):
        """
        Test logging functions.

        Test :func:`~verboselogs.VerboseLogger.verbose()`,
        :func:`~verboselogs.VerboseLogger.notice()`, and
        :func:`~verboselogs.VerboseLogger.spam()`.
        """
        for name in 'notice', 'verbose', 'spam':
            logger = verboselogs.VerboseLogger(random_string())
            logger._log = mock.MagicMock()
            level = getattr(verboselogs, name.upper())
            method = getattr(logger, name.lower())
            message = "Any random message"
            method(message)
            logger._log.assert_called_with(level, message, ())

    def test_pylint_plugin(self):
        """Test the :mod:`verboselogs.pylint` module."""
        saved_args = sys.argv
        try:
            sys.argv = ['pylint', '--load-plugins', 'verboselogs.pylint', '--errors-only', 'verboselogs']
            __import__('pylint').run_pylint()
        except SystemExit:
            pass
        finally:
            sys.argv = saved_args


def random_string(length=25):
    """Generate a random string."""
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
