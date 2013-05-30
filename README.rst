verboselogs: Verbose logging for Python's logging module
========================================================

The ``verboselogs.VerboseLogger`` class extends `logging.Logger`_  to add the
log level ``VERBOSE``. This log level sits between the predefined ``INFO`` and
``DEBUG`` levels. The code to do this is simple and short, but I still don't
want to copy/paste it to every project I'm working on, hence this module. The
table below shows the names, `numeric values`_ and descriptions_ of the
predefined log levels and the ``VERBOSE`` level defined by this module. I've
added some notes to the other levels, these are marked in bold:

========  =============  =====================================================
Level     Numeric value  Description
========  =============  =====================================================
NOTSET    0              When a logger is created, the level is set to NOTSET
                         (note that the root logger is created with level
                         WARNING). **In practice this level is never explicitly
                         used; it's mentioned here only for completeness.**
DEBUG     10             Detailed information, typically of interest only when
                         diagnosing problems. **Usually at this level the
                         logging output is so low level that it's not useful to
                         users who are not familiar with the software's
                         internals.**
VERBOSE   15             **Detailed information that should be understandable
                         to experienced users to provide insight in the
                         software's behavior; a sort of high level debugging
                         information.**
INFO      20             Confirmation that things are working as expected.
WARNING   30             An indication that something unexpected happened, or
                         indicative of some problem in the near future (e.g.
                         ‘disk space low’). The software is still working as
                         expected.
ERROR     40             Due to a more serious problem, the software has not
                         been able to perform some function.
CRITICAL  50             A serious error, indicating that the program itself
                         may be unable to continue running.
========  =============  =====================================================

Usage
-----

It's very simple to start using the ``verboselogs`` module::

   import logging, verboselogs
   logger = verboselogs.VerboseLogger('verbose-demo')
   logger.addHandler(logging.StreamHandler())
   logger.setLevel(logging.VERBOSE)
   logger.verbose("Can we have verbose logging? %s", "Yes we can!")

Here's a skeleton of a very simple Python program with a command line interface
and configurable logging::

   """
   Usage: demo.py [OPTIONS]

   This is the usage message of demo.py. Usually
   this text explains how to use the program.

   Supported options:
     -v, --verbose  make more noise
     -h, --help     show this message and exit
   """

   import getopt
   import logging
   import sys
   import verboselogs

   logger = verboselogs.VerboseLogger('demo')
   logger.addHandler(logging.StreamHandler())
   logger.setLevel(logging.INFO)

   # Command line option defaults.
   verbosity = 0

   # Parse command line options.
   opts, args = getopt.getopt(sys.argv[1:], 'vh', ['verbose', 'help'])

   # Map command line options to variables.
   for option, argument in opts:
       if option in ('-v', '--verbose'):
           verbosity += 1
       elif option in ('-h', '--help'):
           print __doc__.strip()
           sys.exit(0)
       else:
           assert False, "Unhandled option!"

   # Configure logger for requested verbosity.
   if verbosity >= 2:
       logger.setLevel(logging.DEBUG)
   elif verbosity >= 1:
       logger.setLevel(logging.VERBOSE)

   # Your code goes here.
   ...

Contact
-------

The latest version of ``verboselogs`` is available on PyPi_ and GitHub_
(although I don't suppose it will ever change, since it's so incredibly
simple). For bug reports please create an issue on GitHub_. If you have
questions, suggestions, etc. feel free to send me an e-mail at
`peter@peterodding.com`_.

License
-------

This software is licensed under the `MIT license`_.

© 2013 Peter Odding.

.. External references:
.. _GitHub: https://github.com/xolox/python-verboselogs
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPi: https://pypi.python.org/pypi/verboselogs
.. _logging.Logger: http://docs.python.org/2/library/logging.html#logger-objects
.. _numeric values: http://docs.python.org/2/howto/logging.html#logging-levels
.. _descriptions: http://docs.python.org/2/howto/logging.html#when-to-use-logging
