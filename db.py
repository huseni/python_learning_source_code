__author__ = 'kathiria'

def get_db2_binary_fixpack_version(STAGE_DIRECTORY):
    """
    This method is to find DB2 version from the unzip binary
    """
    val = ""
    path_for_base_db2_file = ""
    db2_version_list = ['10.1', '10.5', '9.7', '9.5']
    dir_list = glob.glob("%s/*" % (STAGE_DIRECTORY))
    for elm in dir_list:
        fixpack_type = os.path.split(elm)[-1]
        if fixpack_type.startswith('universal'):
            steplog.info("This is a universal fixpack binary : %s" % fixpack_type)
            server_dirname = elm
            steplog.debug("Server Directory Name : %s " % server_dirname)
            steplog.debug("Stage Directory Path : %s " % STAGE_DIRECTORY)
            if ostools.is_aix():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2', 'aix', 'FILES')
            elif ostools.is_linux():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2', 'linuxamd64', 'FILES')

        elif fixpack_type.startswith('server'):
            steplog.info("This is a server fixpack binary : %s" % fixpack_type)
            server_dirname = elm
            steplog.debug("Server Directory Name : %s " % server_dirname)
            steplog.debug("Stage Directory Path : %s " % STAGE_DIRECTORY)
            if ostools.is_aix():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2', 'aix', 'FILES')
            elif ostools.is_linux():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2', 'linuxamd64', 'FILES')


    if os.path.exists(path_for_base_db2_file):
        steplog.info("DB2 binary is found and it is uncompressed")
        try:
            files = os.listdir(path_for_base_db2_files)
            for item in files:
                if item.startswith('INSTANCE_SETUP_SUPPORT_'):
                    val = item
                    steplog.info("Found the file to extract the fixpack version : %s" % val)
                    break
            s1 = re.compile(r'_(\d+\.\d+)\.', re.DOTALL)
            match_found = s1.search(val)
            if match_found:
                db2_version_from_file = match_found.group(1)
                if db2_version_from_file in db2_version_list:
                    steplog.info("This is the valid DB2 version : %s" % db2_version_from_file)
                    pat = re.compile(r"INSTANCE_SETUP_SUPPORT_\d+\.\d+\.\d+\.(\d+)_")
                    fp_found = pat.search(val)
                    return fp_found.group(1)
                else:
                    return False
        except IOError:
            steplog.info('There is no file exists')
    else:
        steplog.info("DB2 binary may have not unzipped")
