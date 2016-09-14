def get_db2_binary_build_version(STAGE_DIRECTORY):
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
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2')
            elif ostools.is_linux():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2')
                
        elif fixpack_type.startswith('server'):
            steplog.info("This is a server fixpack binary : %s" % fixpack_type)
            server_dirname = elm
            steplog.debug("Server Directory Name : %s " % server_dirname)
            steplog.debug("Stage Directory Path : %s " % STAGE_DIRECTORY)
            if ostools.is_aix():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2')
            elif ostools.is_linux():
                path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2')
           
       
    if os.path.exists(path_for_base_db2_file):
        steplog.info("DB2 binary is found and it is uncompressed")
        try:
            files = os.listdir(path_for_base_db2_files)
            for item in files:
                if item.startswith('spec'):
                    val = item
                    steplog.info("Found the file to extract the fixpack version : %s" % val)
                    break
            spec_file = os.path.join(path_for_base_db2_file, 'spec')
            if os.path.isfile(spec_file):
                with open(spec_file) as fh:
                    for line in fh:
                        if "special_" in line:
                            build_level_list = line.split('=")
                            build_level = build_level_list[-1]
                            steplog.info("Special fixpack build level : %s " % build_level)
                            break
                return build_level    
        except IOError:
            steplog.info('There is no file exists')
    else:
        steplog.info("DB2 binary may have not unzipped")