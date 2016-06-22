"""
Verbose and spam log levels for Python's logging module.

Author: Peter Odding <peter@peterodding.com>
Last Change: June 22, 2016
URL: https://pypi.python.org/pypi/verboselogs
"""

import logging

# Semi-standard module versioning.
__version__ = '1.2'


def add_log_level(value, name):
    """
    Add a new log level to the :mod:`logging` module.

    :param value: The log level's number (an integer).
    :param name: The name for the log level (a string).
    """
    logging.addLevelName(value, name)
    setattr(logging, name, value)


# Create the VERBOSE log level (between INFO and DEBUG).
add_log_level(15, 'VERBOSE')

# Create the SPAM log level (between DEBUG and NOTSET).
add_log_level(5, 'SPAM')


class VerboseLogger(logging.Logger):

    """
    Custom logger class that supports the additional logging levels 'verbose'
    (with a severity between 'info' and 'debug') and 'spam' (with a severity
    between 'debug' and 'notset').
    """

    def __init__(self, *args, **kw):
        """
        Initialize the superclass and set the root logger as the parent of this
        logger. The function :func:`logging.getLogger()` is normally
        responsible for defining the hierarchy of logger objects however
        because verbose loggers are created by calling the
        :class:`VerboseLogger` constructor, we're responsible for defining the
        parent relationship ourselves.
        """
        logging.Logger.__init__(self, *args, **kw)
        self.parent = logging.getLogger()

    def verbose(self, *args, **kw):
        """
        Log a verbose message: A message that we would like to log in verbose
        mode (-v) as a sort of high level debugging information (whereas
        logger.debug() is used to log low level information). This method has
        the same contract as the existing methods for logging a message.
        """
        self.log(logging.VERBOSE, *args, **kw)

    def spam(self, *args, **kw):
        """
        Log a spam message: A message that we would like to log in case
        someone is getting desperate in a late night debugging session and
        decides that he wants as much instrumentation as possible :-).
        """
        self.log(logging.SPAM, *args, **kw)
