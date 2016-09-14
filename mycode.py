__author__ = 'kathiria'

import os
import steplog
import sys


def prepare_db2_hadr_service_config():
    hadr_dft_config_dict = {'hadr_local_host': 'sybaselab13.usa.hp.com', 'hadr_local_svc': 'DB2_HADR_PORT_V105', 'hadr_remote_host':
                            'sybaselab14.usa.hp.com', 'hadr_remote_svc': 'DB2_HADR_PORT_V105', 'hadr_remote_inst': 'v105user',
                            'hadr_timeout': '120', 'hadr_syncmode': 'nearsync', 'hadr_peer_window': '300'}

    for config_param in hadr_dft_config_dict:
        print "Original config : hadr_dft_config_dict['%s']: %s" % (config_param, hadr_dft_config_dict[config_param])
        if config_param == params['DB2 HADR Peer Window']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Peer Window']

        if config_param == params['DB2 HADR Port Number']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Port Number']

        if config_param == params['DB2 HADR Primary Host Name']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Primary Host Name']

        if config_param == params['DB2 HADR Remote Instance Name']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Remote Instance Name']

        if config_param == params['DB2 HADR Service Name']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Service Name']

        if config_param == params['DB2 HADR Standby Host Name']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Standby Host Name']

        if config_param == params['DB2 HADR SyncMode']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR SyncMode']

        if config_param == params['DB2 HADR Timeout']:
            hadr_dft_config_dict[config_param] = params['DB2 HADR Timeout']

        print "After modification config : hadr_dft_config_dict['%s']: %s" % (config_param, hadr_dft_config_dict[config_param])

    print "Updated Config Dictionary"
    for config_param, config_value in hadr_dft_config_dict.iteritems():
        print "dict['%s']: %s" % (config_param, config_value)
    print "=================================================================="

    service_file = os.path.join('/tmp', 'db2_hadr_config')
    if os.path.exists(os.path.join('/tmp', 'db2_hadr_config')):
        steplog.warn('db2_hadr_config file already exists. It will be overwritten')
        sys.exit(1)

    for config_param, config_value in hadr_dft_config_dict.iteritems():
        hadr_config_params = "update database configuration for %s using %s %s" % (params['HADR Database Name'], config_param, config_value)
        fh = open(service_file, "rw+")
        try:
            fh.write('%s' % hadr_config_params)
        finally:
            fh.close()