__author__ = 'kathiria'

__version__ = '$Revision: 43176 $'

#### DMA Imports ####
import db2tools
import ostools
import ostype
import parametertools
import glob
import re
import sys
import steplog
import os


def get_installed_fixpack_version(install_path):
    cmd = os.path.join(install_path, "bin", "db2level")
    (out, err, rc) = ostools.run_command(cmd)
    dat = " ".join(out.splitlines())
    pat = re.compile(r'Fix\s+Pack\s+\"(\d+)\"')
    x = pat.search(dat)
    if x is None:
        raise EnvironmentError("Invalid output from db2level")
    return x.group(1)


def get_db2_binary_fixpack_version(STAGE_DIRECTORY):
    """
    This method is to find DB2 version from the unzip binary
    """
    val = ""
    dirnames = glob.glob("%s/%s" % (STAGE_DIRECTORY, "server*"))
    #dirnames = glob.glob("%s/%s" % (STAGE_DIRECTORY, "universal*"))
    dirname = dirnames[0]
    server_dirname = os.path.split(dirname)[-1]
    db2_version_list = ['10.1', '10.5', '9.7', '9.5']
    if server_dirname
    path_for_base_db2_file = ""
    if ostools.is_aix():
        path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2', 'aix', 'FILES')
    elif ostools.is_linux():
        path_for_base_db2_files = os.path.join(STAGE_DIRECTORY, server_dirname, 'db2', 'linuxamd64', 'FILES')
    else:
        steplog.warn("Media contains unsupported OS")
        return False
    if os.path.exists(path_for_base_db2_file):
        steplog.info("DB2 binary is found and it is uncompressed")
        try:
            files = os.listdir(path_for_base_db2_files)
            for item in files:
                if item.startswith('INSTANCE_SETUP_SUPPORT_'):
                    val = item
                    steplog.info(" We found the file for finding the version : %s" % val)
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
        steplog.info("DB2 binary have not unzipped")


def main():
    Instance_line={}
    params = parametertools.parse_dma_params()
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
    if not int(media_fixpack) > int(inst_fix_pack):
        steplog.error("A greater version or same version of Fix pack %s is already installed" % inst_fix_pack)
        sys.exit(1)

    states = get_software_states(db2_install)
    shutdown_software(db2_install, states)
    for key, value in states.items():
        if isinstance(value, list):
            params[key] = ','.join(value)
        else:
            params[key] = value
    parametertools.print_header(params)


def get_software_states(db2_install):
    up_instances, _ = db2_install.get_instance_up_down_states()
    up_licd, _ = db2_install.get_instance_license_daemon_states()
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
