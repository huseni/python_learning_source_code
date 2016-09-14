__author__ = 'kathiria'


class LogingContextManager:
    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        if exec_typ is None:
            print('LoginingContextManager:__exit__:'
                  'Normal Exit Detected')

        else:
            print('LogingContextManager.__exit__:' 'Exception detected''type={}, vale={}, traceback={}'.format(exec_type, exec_val, exec_tb))

