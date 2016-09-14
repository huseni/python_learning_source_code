__author__ = 'kathiria'

def get_uncompressed_binary_file_size(file = None):
    file = "/opt/software/DB2_10.5/v10.5_linuxx64_server.tar.gz"
    keys = []
    values = []
    bin_size_dict = {}
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
            st_list = out.split('\n')
            keys = st_list[0].split()
            values = st_list[1].split()

            print "----------------------------------------"
            print keys
            print values
            print "----------------------------------------"

            if keys:
                if values:
                    bin_size_dict = dict(zip(keys, values))
                    for k, v in bin_size_dict.iteritems():
                        if k == 'compressed':
                            compressed_size = v
                            print "binary_file_compressed_file_size : %s " % compressed_size
                        if k == 'uncompressed':
                            uncompressed_size = v
                            print "binary_file_uncompressed_file_size : %s " % uncompressed_size
                        if compressed_size and uncompressed_size:
                            return compressed_size, uncompressed_size
                        else:
                            raise "Could not find the binary file size"
