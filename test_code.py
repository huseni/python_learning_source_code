__author__ = 'kathiria'

#### Python/Jython Imports ####
import sys
import os
import re
import threading


#### DMA Imports ####
from validator import Validator
import ostools
import commonvalidation
import pythontools
import parametertools
import steplog
import db2tools


### Globals ###
params = parametertools.parse_dma_params()


def create_backup_dir(params_dict):
    """
    To check and create a backup director path if not found.
    """
    print threading.currentThread().getName(), 'Starting'
    backup_location = params_dict['DB2 Installation Backup Directory']
    if not os.path.exists(backup_location):
        steplog.info("Attempting to create the backup directory")
        try:
            os.makedirs(backup_location)
            steplog.info("Backup directory has been created")
        except OSError:
            if not os.path.isdir(backup_location):
                raise ValueError("Backup directory could not be created")


def validate_db2_installation(db2_home=None):
    """
    To validate and ensure that if the current db2 installation is good without any binary file corruption.
    """
    print threading.currentThread().getName(), 'Starting'
    if not os.path.exists(db2_home):
        return False, "Invalid DB2 installation location specified. Please check"
    if not os.path.exists(os.path.join(db2_home,'bin','db2')):
        return False, "Could not find DB2 command line processor. Installation might have been corrupted or incomplete"
    db2valpath = os.path.join(db2_home, 'bin', 'db2val')
    if not os.path.exists(db2valpath):
        return True, "db2val utility is not available for the current DB2 installation version. db2val cannot be run. Skipping this ..."
    else:
        out, err, rc = ostools.run_command(os.path.join(db2_home, "bin", "db2val"))
    if rc:
        return False, "Failed to run db2val to verify DB2 installation"
    if re.search("db2val command completed successfully. You may proceed", out):
        return True, "DB2 Installation found"
    return False, "Invalid DB2 Installation Directory specified"


def setup_filespace_requirements():
    print threading.currentThread().getName(), 'Starting'
    return {
            'extract': (2, params['DB2 Installation Backup Directory']),
            'install': (3, params['Current DB2 Installation Location']),
            }


def check_required_parameters(required_params_dict=dict()):
    """
    To Check if the required parameters are set by user input or default parameter set through property attributes
    """
    print threading.currentThread().getName(), 'Starting'
    is_valid = True
    required_params_not_set = pythontools.validate_required_parameters(required_params_dict)
    if len(required_params_not_set) > 0:
        is_valid = False
        msg = "Validate all required input parameters are set failed."
        for param in required_params_not_set:
            steplog.error("Required parameter %s is not set." % param)
    else:
        msg = "Validate all required input parameters are set succeeded."
    return is_valid, msg


def print_header(params):
    print threading.currentThread().getName(), 'Starting'
    parametertools.print_header(params)


### Main ###
def main():
    print("-"*80)
    steplog.info('Validating rollback fixpack parameters...')
    print("-"*80)
    if ostools.is_windows():
        steplog.error('This workflow runs on unix platforms only.')
        sys.exit(1)

    p1 = threading.Thread(name='create_backup_dir', target=create_backup_dir, args=(params,))
    p2 = threading.Thread(name='validate_db2_installation', target=validate_db2_installation, args=(params['Current DB2 Installation Location'],))
    p3 = threading.Thread(name='check_required_parameters', target=check_required_parameters, args=(params,))


    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


    Validator.register(commonvalidation.check_filespace_requirements, args=[setup_filespace_requirements()])
    Validator.validate()
    failures = Validator.str_failed_results()
    if failures:
        msg = 'Error(s) validating parameters for Rollback DB2 Fixpack :\n\n%s' % failures
        steplog.info(msg)
        steplog.error(msg)
        sys.exit(1)

    fixpack_number = db2tools.get_installed_fixpack_version(params['Current DB2 Installation Location'])
    params['Fixpack Number'] = fixpack_number
    print_header(params)
    print("-"*80)
    steplog.info('Validation for rollback fixpack parameters successful. You may proceed.')
    print("-"*80)


#### Call to main ####
if __name__ == '__main__':
    try:
        main()
    except StandardError, e:
        steplog.handle_exception(e)
