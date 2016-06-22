# Verbose and spam log levels for Python's logging module.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: June 23, 2016
# URL: https://verboselogs.readthedocs.io

"""
Verbose and spam log levels for Python's :mod:`logging` module.

The :mod:`verboselogs` module defines the :data:`VERBOSE` and :data:`SPAM`
constants, the :class:`VerboseLogger` class and the :func:`add_log_level()` and
:func:`install()` functions. At import time :func:`add_log_level()` is used to
register the custom log levels :data:`VERBOSE` and :data:`SPAM` with Python's
:mod:`logging` module.
"""

import logging

__version__ = '1.3'
"""Semi-standard module versioning."""

VERBOSE = 15
"""
The numeric value of the 'verbose' log level (a number).

The value of :data:`VERBOSE` positions the verbose log level between the
:data:`~logging.INFO` and :data:`~logging.DEBUG` levels.

:see also: The :func:`~VerboseLogger.verbose()` method of the
           :class:`VerboseLogger` class.
"""

SPAM = 5
"""
The numeric value of the 'spam' log level (a number).

The value of :data:`SPAM` positions the spam log level between the
:data:`~logging.DEBUG` and :data:`~logging.NOTSET` levels.

:see also: The :func:`~VerboseLogger.spam()` method of the
           :class:`VerboseLogger` class.
"""


def install():
    """
    Make :class:`VerboseLogger` the default logger class.

    The :func:`install()` function uses :func:`~logging.setLoggerClass()` to
    configure :class:`VerboseLogger` as the default class for all loggers
    created by :func:`logging.getLogger()` after :func:`install()` has been
    called. Here's how it works:

    .. code-block:: python

        import logging
        import verboselogs

        verboselogs.install()
        logger = logging.getLogger(__name__) # will be a VerboseLogger instance
    """
    logging.setLoggerClass(VerboseLogger)


def add_log_level(value, name):
    """
    Add a new log level to the :mod:`logging` module.

    :param value: The log level's number (an integer).
    :param name: The name for the log level (a string).
    """
    logging.addLevelName(value, name)
    setattr(logging, name, value)


# Define the VERBOSE log level.
add_log_level(VERBOSE, 'VERBOSE')

# Define the SPAM log level.
add_log_level(SPAM, 'SPAM')


class VerboseLogger(logging.Logger):

    """
    Custom logger class to support the additional logging levels.

    This subclass of :class:`logging.Logger` adds support for the additional
    logging methods :func:`verbose()` and :func:`spam()`. You can use
    :func:`install()` to make :class:`VerboseLogger` the default logger
    class.
    """

    def __init__(self, *args, **kw):
        """
        Initialize a :class:`VerboseLogger` object.

        :param args: Refer to the superclass (:class:`logging.Logger`).
        :param kw: Refer to the superclass (:class:`logging.Logger`).

        This method first initializes the superclass and then it sets the root
        logger as the parent of this logger.

        The function :func:`logging.getLogger()` is normally responsible for
        defining the hierarchy of logger objects however because verbose
        loggers can be created by calling the :class:`VerboseLogger`
        constructor, we're responsible for defining the parent relationship
        ourselves.
        """
        logging.Logger.__init__(self, *args, **kw)
        self.parent = logging.getLogger()

    def verbose(self, *args, **kw):
        """Log a message with level :data:`VERBOSE`. The arguments are interpreted as for :func:`logging.debug()`."""
        self.log(logging.VERBOSE, *args, **kw)

    def spam(self, *args, **kw):
        """Log a message with level :data:`SPAM`. The arguments are interpreted as for :func:`logging.debug()`."""
        self.log(logging.SPAM, *args, **kw)
