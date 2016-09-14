def audit_601_password_protect_database_backups():
    """Password protect database backups"""
    global conn
    dump_files = io_params['Sybase Dump File List'].strip().split(',')
    
    isValid = True
    msg = ''
    
    for dump_file in dump_files:
        sql = "load database whatisthedatabasename99999999 from \"%s\" with headeronly" % dump_file
        resultq = sybasetools.run_sql_statement(sql, BASE_SQL, SYBASE_SERVER, SYBASE_USER, SYBASE_PASSWORD, SYBASE_OS_USER, SYBASE_HOME, do_query=False)
        lines = resultq.splitlines()
        database_name = ''
        for line in lines:
            if line.find('This is a database dump of database ID') > -1:
                tokens = line.split(',')
                lst = re.findall('\w+',tokens[1])
                database_name = lst[1]
                break        
                
        sql = """load database %s from \'%s\' with headeronly""" % (database_name,dump_file)
        
        
        result = sybasetools.run_sql_statement(sql, BASE_SQL, SYBASE_SERVER, SYBASE_USER, SYBASE_PASSWORD, SYBASE_OS_USER, SYBASE_HOME, do_query=False)
        
        if result.find('Dump is password-protected, a valid password is required') > -1:
            isValid = True
            msg = 'Database %s is password-protected and is secure' % dump_file
            steplog.info(msg)
        else:
            isValid = False
            msg = 'Database %s is not password-protected and is not secure' % dump_file
            steplog.warn(msg)
            break
            
    if isValid == True:
        msg = 'Database files %s are password-protected and secure' % (io_params['Sybase Dump File List'].strip())
    return isValid, msg