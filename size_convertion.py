__author__ = 'kathiria'


def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

size = sizeof_fmt(2727987200)
print size


def get_uncompressed_binary_file_size(file = None):
    if not file:
        raise "Value Error. No input file is provided"
    else:
        cmd = 'zip'