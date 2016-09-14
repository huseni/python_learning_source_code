__author__ = 'kathiria'


def conv_MB_to_GB(input_megabyte):
    gigabyte = float(9.5367431640625E-7)
    convert_gb = gigabyte * input_megabyte
    return convert_gb


GB = conv_MB_to_GB(958.6)
print GB

def bytesto(bytes, to, bsize=1024):
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))

       sample output:
           mb= 300002347.946
    """

    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize

    return(r)


GB1 = bytesto(1005168640, 'g')
print "%s" % GB1
GB2 = bytesto(916383713, 'g')
print GB2

def bytesto(bytes, to, bsize=1024):
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))

       sample output:
           mb= 300002347.946
    """

    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize
    return(r)


def get_uncompressed_binary_file_size(file = None):
    bin_file = os.path.join(params['Download Location'], params['DB2 Fixpack Software Binaries'])
    #file = "/opt/software/fixpack/v10.1fp4_linuxx64_universal_fixpack.tar.gz"
    keys = []
    values = []
    bin_size_dict = {}
    if not os.path.exists(bin_file):
        steplog.warn("Binary file must be provided to calculate the size")
        return
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


def setup_filespace_requirements():
    """
    setup file space requirements based on estimated file size.
    """
    std_filespace_setup = {'download': (2, params['Download Location']),'extract': (4, params['Staging Directory']),'install': (4, params['DB2 Installation Location']),}
    linux_file_space_setup = {}
    print "-----------------------------------------------------------"
    print params['DB2 Fixpack Software Binaries']
    print "-----------------------------------------------------------"
    if params['DB2 Fixpack Software Binaries']:
        bin_file = os.path.join(params['Download Location'], params['DB2 Fixpack Software Binaries'])
        if os.path.exists(bin_file):
            compressed_size, uncompressed_size = get_uncompressed_binary_file_size()
            steplog.info("-----------------Byte to GB conversion started ---------------")
            uncompressed_size = int(uncompressed_size)
            compressed_size = int(compressed_size)
            uncompressed_bin_file_size = bytesto(uncompressed_size, 'g')
            print uncompressed_bin_file_size
            compressed_bin_file_size = bytesto(compressed_size, 'g')
            print compressed_bin_file_size
            steplog.info("-----------------Byte to GB conversion completed ---------------")

            ### Calculate and update the estimated disk space requirements for Linux targets ###
            disk_space_dict = {'download': [2, params['Download Location']], 'extract': [4, params['Staging Directory']], 'install': [4, params['DB2 Installation Location']], }
            if uncompressed_bin_file_size:
                disk_space_dict['extract'][0] = uncompressed_bin_file_size
                if ostype.is_linux():
            #return "{'download': (%s, params['Download Location']),     'extract': (%s, params['Staging Directory']), 'install': (4, params['DB2 Installation Location']),}"  % (compressed_bin_file_size, uncompressed_bin_file_size)
                    return disk_space_dict

        else:
            return {'download': (2, params['Download Location']),
                    'extract': (4, params['Staging Directory']),
                    'install': (4, params['DB2 Installation Location']),}

        Validator.register(commonvalidation.check_filespace_requirements, args=[setup_filespace_requirements()])