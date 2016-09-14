#### Python/Jython Imports ####
import sys


### DMA Imports ###
import steplog
import ostools
import parametertools
import db2tools


# GLOBAL DICT #
params = parametertools.parse_dma_params()


def main():
    print("-"*80)
    steplog.info("Verify post rollback fixpack")
    print("-"*80)

    steplog.info('Comparing instance version with fixpack version that you want to rollback.')
    fixpack_version, instance_version = db2tools.get_instance_version(params['DB2 Installation Location'])
    print("Current instance version", instance_version)
    print("-"*80)
    if int(instance_version) == int(params['Fixpack Number']):
        steplog.error("Fixpack level matchs: %s = %s. Rollback did not occur" % (instance_version, params['Fixpack Number']))
        return_code = 1
    else:
        steplog.info("Fixpack level do not match: %s != %s. Fixpack successfully rolled back." % (instance_version, params['Fixpack Number']))
        return_code = 0
    print("-"*80)
    sys.exit(return_code)

db2_profile = "/sqllib/db2profile"
import os


def is_non_zero_file(file_path=None):
    """
    Check if the file is non-empty and the given path is a file and not the directory
    Usage:
            valid_file = is_non_zero_file(db2_profile)
    """
    return True if os.path.isfile(file_path) and os.path.getsize(file_path) > 0 else False


def get_database_list(instance=None):
    """
    This function is to extract and return the list of databases on the given target DB2 Instance.
    Usage:
            database_list = get_database_list('db2inst1')
            db_list = [database for database in database_list]
    """
    databases = list()
    global db2_profile
    steplog.info('Pull the list of databases from the current instance.')
    if not instance:
        raise ValueError("You must provide the DB2 instance name")

    if not db2_profile:
        raise SystemError("Missing db2profile default path")

    if is_non_zero_file(db2_profile):
        cmd = '. ~%s/%s ; cd / ; db2 list database directory | grep "Database name"' % (instance, db2_profile)
        out, err, rc = db2tools.run_instance_command(instance, cmd)
        steplog.debug(out)
        steplog.debug(rc)
        if rc == 0:
            if out:
                for line in out.splitlines():
                    if line.strip().startswith('Database name'):
                        database_name = line.split('=')[1].strip()
                        databases.append(database_name)
                return databases
            else:
                steplog.info("No database found for the current instance: %s" % instance)
        else:
            raise EnvironmentError("Command could not run successfully. Please check again")


#### Call to main() ####
if __name__ == '__main__':
    try:
        main()
    except StandardError, e:
        steplog.handle_exception(e)