from __future__ import with_statement
__version__ = '$Revision: 43176 $'

#### DMA Imports ####
import db2tools
import ostools
import ostype
import parametertools

### Python Imports ###
import glob
import re
import sys
import steplog
import os

### GLOBAL ###
params = parametertools.parse_dma_params()

def get_installed_fixpack_version(install_path):
    cmd = os.path.join(install_path, "bin", "db2level")
    (out, err, rc) = ostools.run_command(cmd)
    dat = " ".join(out.splitlines())
    pat = re.compile(r'Fix\s+Pack\s+\"(\d+)\"')
    x = pat.search(dat)
    if x is None:
        raise EnvironmentError("Invalid output from db2level")
    return x.group(1)


def get_installed_fixpack_build(install_path):
    cmd = os.path.join(install_path, "bin", "db2level")
    out, err, rc = ostools.run_command(cmd)
    lines = " ".join(out.splitlines())
    match = re.compile(r'special_(\d+)')
    match_found = match.search(lines)
    if match_found:
        return match_found.group(1)
    else:
        return ''


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
                    steplog.debug("File to extract the fixpack version build number : %s" % val)
                    spec_file = os.path.join(path_for_base_db2_files, 'spec')
                    
                    if os.path.isfile(spec_file):
                        print ("Spac file exists and reading")
                        with open(spec_file) as fh:
                            for line in fh:
                                if "special_" in line:
                                    build_level_list = line.split("=")
                                    build_level = build_level_list[-1]
                                    build_num = build_level[8:]
                                    steplog.info("Special fixpack build level : %s " % build_num)
                                    return build_num    
        except IOError:
            steplog.info('There is no file exists')
    else:
        steplog.info("DB2 binary may have not unzipped")
        
        
def main():
    steplog.info("------------------------------------------------------")
    steplog.info("Shutting down the DB2 Instances to patch fixpack")
    steplog.info("------------------------------------------------------")
    
    Instance_line={}
   # params = parametertools.parse_dma_params()
    install_path = params['Install Path']
    db2_install = db2tools.DB2Installation(install_path)
    db2_install.find_instances_and_das()
    
    ## Extract the instance details found on the target machine ##
    Instance_line = db2_install.instances
    
    ## First Instance in the instances found on the target ##
    if Instance_line:
        first_inst_name = Instance_line.keys()[0]
        instance_to_set = first_inst_name
        steplog.debug(first_inst_name)
        
    if instance_to_set:
        ## Setup the default DB2 Instance on target machine environment ##
        os.environ["DB2INSTANCE"] = instance_to_set.strip()
        steplog.debug(os.environ["DB2INSTANCE"])
                      

    inst_fix_pack = get_installed_fixpack_version(install_path)
    media_fixpack = get_db2_binary_fixpack_version(params['Stage Archive'])
    custom_fixpack = params['If Custom Fixpack']
    custom_fixpack = custom_fixpack.strip()
    
    print custom_fixpack
    
    if custom_fixpack== "true" or custom_fixpack == "yes" or custom_fixpack == "y":
        steplog.info("The current version of fixpack determined from the binary is of the same version as of on the target. Custom fixpack will be installed")
        inst_fix_build_num = get_installed_fixpack_build(params['Install Path'])
        print "Installed fixpack build : %s" % inst_fix_build_num
        media_build_num = get_db2_binary_build_version(params['Stage Archive'])
        if not media_build_num or inst_fix_build_num:
            if not int(media_build_num) > int(inst_fix_build_num):
                steplog.error("A greater version or same version of Fixpack build %s is already installed" % inst_fix_build_num)
                sys.exit(1)
            
    else:    
        if not int(media_fixpack) > int(inst_fix_pack):
            steplog.error("A greater version or same version of Fix pack %s is already installed" % inst_fix_pack)
            sys.exit(1)
    
    states = get_software_states(db2_install, install_path)
    shutdown_software(db2_install, states)
    for key, value in states.items():
        if isinstance(value, list):
            params[key] = ','.join(value)
        else:
            params[key] = value
    parametertools.print_header(params)


def get_software_states(db2_install, install_path):
    up_instances, _ = db2_install.get_instance_up_down_states()
    up_licd, _ = db2_install.get_instance_license_daemon_states()
    custom_fixpack = params['If Custom Fixpack'] 
    if custom_fixpack== "true" or custom_fixpack == "yes" or custom_fixpack == "y": 
        fixpack_build_num = get_installed_fixpack_version(install_path)
    else:
        fixpack_build_num = None
    is_das_up = False if db2_install.das is None else db2_install.das.up_down == 'up'
    is_fmc_up = db2_install.get_fmc_pid() is not None
    auto_starts = []
    if is_fmc_up:
        auto_starts, _ = db2_install.get_auto_start_states()

    states = {
        'Up Instances': up_instances,
        'Up LICDs': up_licd,
        'Is DAS Up': is_das_up,
        'Auto Starts': auto_starts,
        'Fixpack Build Number' : fixpack_build_num,
    }
    return states


def shutdown_software(db2_install, states):

    db2_install.force_applications_shutdown()
    db2_install.terminate_instances()
    db2_install.set_instance_up_down_states(offs=states['Up Instances'])
    db2_install.set_instance_license_daemon_states(offs=states['Up LICDs'])
    if states['Is DAS Up']:
        db2_install.das.up_down = 'down'
    if ostype.is_aix():
        ostools.run_command('/usr/sbin/slibclean')
    auto_starts = states['Auto Starts']
    if auto_starts:
        db2_install.set_auto_start_states(offs=auto_starts)
    db2_install.ip_clean_instances()


if __name__ == '__main__':
    main()