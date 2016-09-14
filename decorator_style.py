__author__ = 'kathiria'


def smart_divide(func):
    def inner(a, b):
        a -= 1
        b += 2
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        else:
            print ("I am good and dividable")

        return func(a, b)
    return inner


@smart_divide
def divide(a,b):
    return a/b


divide(2,5)
divide(2,0)


def star(func):
    def inner(*args, **kwargs):
        print ("*" * 30)
        print " inside star start"
        func(*args, **kwargs)
        print " inside star end"
        print ("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print ("%" * 30)
        print "inside percent start"
        func(*args, **kwargs)
        print "inside percent end"
        print("%" * 30)
    return inner

@percent
@star
def printer(msg):
    print(msg)


printer("This python decorator is written by Huseni")


from functools import wraps

def print_name(decorating_fun):
    @wraps(decorating_fun)
    def d_wrapper(fname, lname):
        """
        This is the d_wrapper function part of decorator function wrapper
        """
        print "starting - In decorating fun"
        print fname + "bhai" + lname
        new_name = decorating_fun(lname)
        print new_name
        print "ending - In decorating fun"
    return d_wrapper

@print_name
def print_full_name(lname):
    """
    This is the original print_full_name function
    """
    return "Mr." + lname


print_full_name('huseni', 'kathiria')
print print_full_name.__name__
print print_full_name.__doc__



def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            ff = "<{0}>{1}</{0}>".format(tag_name, func(name))
            print "calling ff tag" + ff
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name
print get_text("John")

@tags("simple")
def get_text(name):
    return "Hello "+name
#print get_text("John")

@tags("easy")
def get_text(name):
    return "Hello "+name

#print get_text("John")
print "********************************************************"


def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname()


def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print my_person.get_fullname()













def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

size = sizeof_fmt(2727987200)
print size


def get_uncompressed_binary_file_size(file = None):
    file = "/opt/software/DB2_10.5/v10.5_linuxx64_server.tar.gz"
    keys = []
    values = []
    bin_size_dict = {}
    if not file:
        raise "Value Error. No input file is provided"
    else:
        command = 'gzip -l %s' % file
        steplog.info("command : %s" % command)
        out, err, rc = ostools.run_command(command)
        print "output : %s " % out
        print "error : %s " % err
        print "rc : %s " % rc

        if rc == 0:
            st_list = out.split('\n')
            for line in st_list:
                if "compressed" in line:
                    keys = line.split()
                    print "Keys: %s" % keys
                else:
                    values = line.split()
                    print "Values: %s" % values
                if keys:
                    if values:
                        bin_size_dict = dict(zip(keys,values))
                        for k,v in bin_size_dict.iteritems():
                            if k == 'compressed':
                                compressed_size = v
                            if k == 'uncompressed':
                                uncompressed_size = v
                                pass
                        print "binary_file_compressed_file_size : %s " % compressed_size
                        print "binary_file_uncompressed_file_size : %s " % uncompressed_size




def get_db2_binary_fixpack_version(STAGE_DIRECTORY):
    """
    This method is to find DB2 version from the unzip binary
    """
    val = ""
    #dirnames = glob.glob("%s/%s" % (STAGE_DIRECTORY, "server*"))
    #dirnames = glob.glob("%s/%s" % (STAGE_DIRECTORY, "universal*"))
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



















































