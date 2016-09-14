__author__ = 'kathiria'

import contextlib
import sys

@contextlib.contextmanager
def logining_context_manager():
    print('logging_context_manager : enter')
    try:
        yield 'you are in a with block'
        print ('logging_context_manager : normal exit')

    except Exception:
        print('logging_context_manager : exceptional exit', sys.exc_info())
