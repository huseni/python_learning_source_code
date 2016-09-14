__author__ = 'kathiria'

import wrapt
import inspect

@wrapt.decorator
def universal(wrapped, instance, args, kwargs):
    if instance is None:
        if inspect.isclass(wrapped):
            # Decorator was applied to a class.
            return wrapped(*args, **kwargs)
        else:
            # Decorator was applied to a function or staticmethod.
            return wrapped(*args, **kwargs)
    else:
        if inspect.isclass(instance):
            # Decorator was applied to a classmethod.
            return wrapped(*args, **kwargs)
        else:
            # Decorator was applied to an instancemethod.
            return wrapped(*args, **kwargs)


def setup_filespace_requirements():
    """
    setup file space requirements based on estimated file size.
    """
    if params['DB2 Fixpack Software Binaries']:
        bin_file = os.path.join(params['Download Location'], params['DB2 Fixpack Software Binaries'])
        if ostype.is_linux():
            if os.path.exists(bin_file) and os.path.isfile(bin_file):
                compressed_size, uncompressed_size = postools.get_uncompressed_binary_file_size(params['Download Location'], params['DB2 Fixpack Software Binaries'])
                steplog.debug("-----------------Byte to GB conversion started ---------------")
                uncompressed_size = int(uncompressed_size)
                compressed_size = int(compressed_size)
                uncompressed_bin_file_size = postools.bytesto(uncompressed_size, 'g')

                print uncompressed_bin_file_size
                compressed_bin_file_size = postools.bytesto(compressed_size, 'g')
                print compressed_bin_file_size
                steplog.debug("-----------------Byte to GB conversion completed ---------------")

                disk_space_dict = {'download': [2, params['Download Location']], 'extract': [4, params['Staging Directory']], 'install': [4, params['DB2 Installation Location']], }
                if uncompressed_bin_file_size:
                    disk_space_dict['extract'][0] = uncompressed_bin_file_size
                    return disk_space_dict
            else:
                return {'download': (2, params['Download Location']),
                    'extract': (4, params['Staging Directory']),
                        'install': (4, params['DB2 Installation Location']),}
        else:
            return {'download': (2, params['Download Location']),
                    'extract': (4, params['Staging Directory']),
                    'install': (4, params['DB2 Installation Location']),}
    else:
        return {'download': (2, params['Download Location']),
                'extract': (4, params['Staging Directory']),
                'install': (4, params['DB2 Installation Location']),}