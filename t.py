def update_primary_hadr_acr_config():
    """
    To configure DB2 HADR using TSA file system on primary node
    """
    global dma_config_loc
    global hadr_tsa_config_file
    global user_group
    
    if params['User Defined Standby HADR TSA Config File']:
        service_file = os.path.join(params['DB2 Archive Location'], params['User Defined Standby HADR TSA Config File'])    
        if os.path.exists(service_file):
            postools.set_file_owner(service_file, params['DB2 HADR Local Instance Name'])
            postools.set_file_group(service_file, user_group)
            cmd = '. ~%s/sqllib/db2profile ; cd / ; db2haicu -f %s' % (params['DB2 HADR Local Instance Name'], service_file)
    else:
        steplog.error("No TSA configuration xml file found to activate ACR. Please check")
        sys.exit(1)
           
    steplog.debug("Command to run : %s " % cmd)
    out, err, rc = db2tools.run_instance_command(params['DB2 HADR Local Instance Name'], cmd)
    steplog.debug("Output %s " % out)
    steplog.debug("Return Code %s " % rc)
    steplog.debug("Error %s " % out)


    if params['User Defined Primary Node Config File']:
        service_file = os.path.join(params['DB2 Archive Location'], params['User Defined Primary Node Config File'])
        if os.path.exists(service_file):
            postools.set_file_owner(service_file, params['DB2 HADR Local Instance Name'])
            postools.set_file_group(service_file, user_group)
            cmd = '. ~%s/sqllib/db2profile ; cd / ; db2 -tvf %s' % (params['DB2 HADR Local Instance Name'], service_file)
    else:
        service_file = os.path.join(dma_config_loc, hadr_config_file)
        if os.path.exists(service_file):
            cmd = '. ~%s/sqllib/db2profile ; cd / ; db2 -tvf %s' % (params['DB2 HADR Local Instance Name'], service_file)

    steplog.debug("Command to run : %s " % cmd)
    out, err, rc = db2tools.run_instance_command(params['DB2 HADR Local Instance Name'], cmd)
    steplog.debug("Output %s " % out)
    steplog.debug("Return Code %s " % rc)





    if params['User Defined Primary HADR TSA Config File']:
        service_file = os.path.join(params['DB2 Archive Location'], params['User Defined Primary HADR TSA Config File'])
        if os.path.exists(service_file):
            postools.set_file_owner(service_file, params['DB2 HADR Remote Instance Name'])
            postools.set_file_group(service_file, user_group)
            cmd = '. ~%s/sqllib/db2profile ; cd / ; db2haicu -f %s' % (params['DB2 HADR Remote Instance Name'], service_file)
    else:
        service_file = os.path.join(dma_config_loc, hadr_tsa_config_file)
        if os.path.exists(service_file):
            cmd = '. ~%s/sqllib/db2profile ; cd / ; db2haicu -f %s' % (params['DB2 HADR Remote Instance Name'], service_file)
            postools.set_file_owner(service_file, params['DB2 HADR Remote Instance Name'])
            postools.set_file_group(service_file, user_group)



    steplog.debug("Command to run : %s " % cmd)
    out, err, rc = db2tools.run_instance_command(params['DB2 HADR Local Instance Name'], cmd)
    steplog.debug("Output %s " % out)