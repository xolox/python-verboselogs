"""
Verbose log level for Python's logging module.

Author: Peter Odding <peter@peterodding.com>
Last Change: June 30, 2013
URL: https://pypi.python.org/pypi/verboselogs
"""

import logging

# Define the numeric value and label of the verbose level.
logging.VERBOSE = 15
logging.addLevelName(logging.VERBOSE, 'VERBOSE')

class VerboseLogger(logging.Logger):

    """
    Custom logger class that supports the additional logging level
    'verbose' whose severity sits between 'info' and 'debug'.
    """

    def __init__(self, *args, **kw):
        """
        Initialize the superclass and set the root logger as the parent of this
        logger. The function :py:func:`logging.getLogger()` is normally
        responsible for defining the hierarchy of logger objects however
        because verbose loggers are created by calling the
        :py:class:`VerboseLogger` constructor, we're responsible for defining
        the parent relationship ourselves.
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
