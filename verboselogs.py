"""
Verbose log level for Python's logging module.

Author: Peter Odding <peter@peterodding.com>
Last Change: May 30, 2013
URL: https://pypi.python.org/pypi/verboselogs
"""

import logging

# Define the numeric value and label of the verbose level.
logging.VERBOSE = 15
logging.addLevelName(logging.VERBOSE, 'VERBOSE')

class VerboseLogger(logging.Logger):

    """
    Custom logger class that supports the additional logging level
    "verbose" whose severity sits between "info" and "debug".
    """

    def __init__(self, *args, **kw):
        """
        Initialize the superclass and define the custom "verbose" log level.
        """
        logging.Logger.__init__(self, *args, **kw)

    def verbose(self, *args, **kw):
        """
        Log a verbose message: A message that we would like to log in verbose
        mode (-v) as a sort of high level debugging information (whereas
        logger.debug() is used to log low level information). This method has
        the same contract as the existing methods for logging a message.
        """
        self.log(logging.VERBOSE, *args, **kw)
