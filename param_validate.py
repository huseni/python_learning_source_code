__author__ = 'kathiria'

import os.path
import ostools


def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

size = sizeof_fmt(2727987200)
print size


def get_uncompressed_binary_file_size(file = None):
    file = "v10.5_linuxx64_server.tar.gz"
    keys = []
    values = []
    if not file:
        raise "Value Error. No input file is provided"
    else:
        command = 'gzip -l %s' % file
        steplog.info("command : %s" % command)
        out, err, rc = ostools.run_command(command)
        print "output : %s " % out
        print "error : %s " % err
        print "rc : %s " % rc

        if rc == 0:
            for line in out.readline():
                if "compressed" in line:
                    keys = line.split()
                else:
                    values = line.split()
            if keys and values:
                bin_size_dict = dict(zip(keys, values))
            compressed_size = keys['compressed']
            uncompressed_size = keys['uncompressed']
            print "compressed_size : %s " % compressed_size
            print "uncompressed_size : %s" % uncompressed_size


get_uncompressed_binary_file_size(v10.5_linuxx64_server.tar.gz)


def validate_db2_software_binaries():
    """
    Validate DB2 Software Binaries
    """
    global is_binary_exists
    #params['DB2 Software Binaries'] = os.path.basename(params['DB2 Software Binaries'])
    if not params['DB2 Software Binaries']:
        steplog.error('Please provide the DB2 software binaries path')
        msg = "Please Provide the DB2 software binaries Path"
        return False, msg
    is_valid = False
    if os.path.isabs(params['DB2 Software Binaries']):
        msg = "Please provide the DB2 software binaries filename without the absolute path"
        steplog.error('Please provide the DB2 software binary filename without the absolute path %s' % params['DB2 Software Binaries'])
        is_valid = False
    else:
        archive = os.path.join(params['DB2 Archive Location'], params['DB2 Software Binaries'])
        if os.path.isfile(archive):
            steplog.debug('Archive %s located' % params['DB2 Software Binaries'])
            is_valid = True
            is_binary_exists = True
            msg = "Software binary %s validated succesfully" % params['DB2 Software Binaries']
        else:
            steplog.debug('Unable to locate the Binaries (%s), will attempt to download from repository' % params['DB2 Software Binaries'])
            steplog.debug('File will be downloaded to (%s)' % archive)
            msg = 'File will be downloaded to (%s)' % archive
            is_valid = True
    return is_valid, msg