__author__ = 'kathiria'

import os
import ostools
import ostype
import sybasetools


def get_current_sp_number(syb_home):
    params = set_params()
    sybase_shell = os.path.join(syb_home, "SYBASE.sh")
    if ostools.is_linux():
        env_set_cmd = "source %s" % sybase_shell
    elif ostools.is_aix() or ostype.is_solaris():
        env_set_cmd = ". %s" % sybase_shell
    data_server_name = params['Sybase Dataserver Name'].strip()
    user_name = params['Sybase OS User Account'].strip()
    sybase_admin = "sa"
    sybase_password = params['Sybase Admin Password'].strip()
    cmd = """%s;isql -Usa -P%s -S %s"""
    cmd %= (env_set_cmd, sybase_password, data_server_name)
    output, err, rc = ostools.sudo_run_command(cmd, user=user_name)
    tmp = ''
    if not rc:
        sql = 'select @@sbssav\ngo'
        result = sybasetools.run_sql_statement(sql, '', data_server_name, sybase_admin, sybase_password, user_name, syb_home, False)
        temp = result.splitlines()
        count = 0
        for line in temp:
            count += 1
            if count == 3:
                words = re.split('\.',line)
                for word in words:
                    tmp = word
                sp_number = tmp
                break
    sp_number_f = float(sp_number)
    return sp_number_f

/opt/sybase/ase157_new/ASE-15_0/bin
[sybase@sybaselab17 bin]$ ./dataserver --sbssav
15.7.0.007


def get_sybase_service_pack(sybase_home):
    """
    Get patch level
    15.7.0.007
    """
    command = 'cd ' + sybase_home + '; . ./SYBASE.sh; dataserver --sbssav'
    try:
        out, _, rc = ostools.sudo_run_command(command, user='sybase')
    except EnvironmentError as ee:
        print(ee.errno, ee.message)
    finally:
    steplog.debug("output from the command:  %s" % out)
    if rc == 0 and out:
        sp_list = out.split('.')
        sp_number = sp_list[-1]
        print("service pack : %d" % int(sp_number))
        return sp_number
    else:
        return ""



    def discover_self(self):
        home = self.get_value('sybase home')
        if not home:
            raise ValueError('No home directory stored in Instance object')
        server_name = self.get_value('server name')
        if not server_name:
            raise ValueError('No server_name stored in Instance object')
        self.set_value('os user', ostools.determine_file_owner(home))
        self.port = sybasetools.get_port_from_interfaces_file(home + '/interfaces', server_name)
        self.set_host()
        self.set_value('sybase version', sybasetools.get_running_sybase_version(home))
        self.set_value('sybase minor version', sybasetools.get_sybase_minor_version(home))
        self.set_value('sybase patch level', sybasetools.get_sybase_patch_level(home))
        self.set_value('sybase esd', sybasetools.get_sybase_esd(home))
        service_pack = get_sybase_service_pack(home)
        if not service_pack == "":
            self.set_value('sybase service pack', get_sybase_service_pack(home))
        sybase_version = sybasetools.get_running_sybase_version(home)
        sybase_version = sybase_version.split('.')[0]
        instance_vers = '%s/%s/%s/%s' % (sybase_version, sybasetools.get_sybase_minor_version(home), sybasetools.get_sybase_patch_level(home), sybasetools.get_sybase_esd(home))
        self.set_value('Version', instance_vers)

        if MODE == "Instance":
            self.user = INST_USER
            self.password = INST_PASS
        return None



