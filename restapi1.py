__author__ = 'kathiria'

import requests

from requests.auth import HTTPBasicAuth

requests.get('https://randomtask.usa.hp.com:8443/dma/sop/workflow/', auth=HTTPBasicAuth('autotest', 'autotest'))
or
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))


def setup_filespace_requirements():
    """
    setup file space requirements based on estimated file size.
    """
    if params['DB2 Fixpack Software Binaries']:
        bin_file = os.path.join(params['Download Location'], params['DB2 Fixpack Software Binaries'])
        if os.path.exists(bin_file):
            if os.path.isfile(bin_file):
                if ostype.is_linux():
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
                    steplog.info("Default required disk space size will be set and validated")
                    return {'download': (2, params['Download Location']),
                            'extract': (4, params['Staging Directory']),
                            'install': (4, params['DB2 Installation Location']),}
            else:
                steplog.warn("Binary file does not exists so size needed for uncompress the file cannot be calculated")
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



def setup_filespace_requirements():
    """
    setup file space requirements based on estimated file size.
    """
    std_filespace_setup = {'download': (2, params['Download Location']),'extract': (4, params['Staging Directory']),'install': (4, params['DB2 Installation Location']),}
    linux_file_space_setup = {}
    if params['DB2 Fixpack Software Binaries']:
        bin_file = os.path.join(params['Download Location'], params['DB2 Fixpack Software Binaries'])
        if os.path.exists(bin_file):
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
                if ostype.is_linux():
                    return disk_space_dict
        else:
            return {'download': (2, params['Download Location']),
                    'extract': (4, params['Staging Directory']),
                    'install': (4, params['DB2 Installation Location']),}