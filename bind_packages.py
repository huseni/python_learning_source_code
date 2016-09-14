__author__ = 'kathiria'

### Python Imports ###
import sys
import os
import os.path
#import mmap

#### DMA Imports ####
import ostools
import steplog
import parametertools
from compliancetools import ComplianceTest
from db2complianceutils import DB2Configuration
from db2tools import connect


def get_databases(instance):
    """
    This function is to extract the list of databases on the given target DB2 Instance
    """
    databases = []
    steplog.info('Getting list of databases.')
    cmd = '. ~%s/sqllib/db2profile ; cd / ; db2 list database directory | grep "Database name"' % instance
    out, err, retCode = db2tools.run_instance_command(instance, cmd)
    steplog.debug(out)
    if out:
        for line in out.splitlines():
            if line.strip().startswith('Database name'):
                database_name = line.split('=')[1].strip()
                databases.append(database_name)
        return databases


def bind_to_database(decorate_binding_process):
    def binding_wrapper(databases, instance):
        print ("I am decorating the database binding process")
        if not databases:
            steplog.warn("No database(s) found on this instance. Database preupgrade check utility cannot be run")
            return ""
        for database in databases:
            dbconn = connect(instance, database)
            sql = decorate_binding_process(instance)
            result_set = dbconn.query_with_db2_shell_prompt(sql, parse = True, use_db2_shell_prompt = True)
            if result_set:
                steplog.debug("Attempting to run the binding....")
                print result_set
            else:
                steplog.warn("Error occured while running the binding of packages with database ")
    return binding_wrapper


@bind_to_database
def bind_db2schema_packages(databases, instance):
    """
    This function is to connect the database and bind the db2schema for the each specific packages.
    """
    db_home = db2tools.get_instance_home(instance)
    sql = 'BIND %s/sqllib/bnd/db2schema.bnd BLOCKING ALL GRANT PUBLIC ACTION ADD SQLERROR CONTINUE' % db_home
    return sql


@bind_to_database
def bind_db2client_packages(databases, instance):
    """
    This function is to connect the database and bind the db2 client for the each specific packages.
    """
    db_home = db2tools.get_instance_home(instance)
    sql = 'db2 BIND %s/sqllib/bnd/@db2cli.lst BLOCKING ALL GRANT PUBLIC ACTION ADD' % db_home
    return sql


@bind_to_database
def bind_db2ubind_packages(databases, instance):
    """
    This function is to connect the database and update the binding for the each specific packages.
    """
    db_home = db2tools.get_instance_home(instance)
    sql = 'db2 BIND %s/sqllib/bnd/@db2ubind.lst BLOCKING ALL GRANT PUBLIC ACTION ADD' % db_home
    return sql


def main():
    print "----------------------------------------------------------------------------------------"
    steplog.info('Binding packages with database objects')
    print "----------------------------------------------------------------------------------------"
    instance_line = {}
    database_list = []
    instance_to_set = ""
    install_path = params['DB2 Installation Location']
    db2_install = db2tools.DB2Installation(install_path)
    db2_install.find_instances_and_das()

    ## Extract the instance details found on the target machine ##
    instance_line = db2_install.instances

    ## First Instance in the instances found on the target ##
    if not instance_line:
        steplog.warn("No instance(s) found for %s DB2 Installation. There is nothing to bind....." % params ['DB2 Installation Location'])
        sys.exit(1)
    else:
        first_inst_name = instance_line.keys()[0]
        if first_inst_name:
            instance_to_set = first_inst_name
        steplog.info("Instances are found in %s DB2 setup. Upgrade process will run.." % params['DB2 Existing Installation Location'])
        steplog.debug(instance_to_set)

    if instance_to_set:
        ## Setup the default DB2 Instance on target machine environment ##
        os.environ["DB2INSTANCE"] = instance_to_set.strip()
        steplog.debug(os.environ["DB2INSTANCE"])

    ## First Instance in the instances found on the target ##
    if instance_line:
        count = len(instance_line)
        for instance in instance_line:
            steplog.info("Instance Counter : %s" % count)
            count -= 1
            instance_to_bind = instance_line.keys()[count]
            steplog.info("Instance found for binding its databases : %s" % instance_to_bind)
            database_list = get_databases(instance_to_bind)
            if database_list:
                bind_db2schema_packages(database_list, instance_to_bind)
                bind_db2client_packages(database_list, instance_to_bind)
                bind_db2ubind_packages(database_list, instance_to_bind)
            else:
                steplog.info("No database found under instance %s. No binding will occure" % instance_to_bind )



if __name__ == '__main__':
    try:
        main()
    except StandardError, e:
        steplog.handle_exception(e)