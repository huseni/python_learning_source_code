#! /usr/bin/python

import shutil
import errno
import os
import sys
import getopt


def backup_db2_installation(src, dst):
    """
    To backup the db2 installation directory.
    """
    check_src_dest_dir(src, dst)
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        print("directory could not be copied")
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise IOError("DB2 installation backup is failed. Please check")


def check_src_dest_dir(src, dst):
    """
    Validate the source and destination directories. if they already exists on the target machine it is good otherwise
    create them on the target.
    """
    if not src:
        raise ValueError("Missing source directory value")
    if not dst:
        raise ValueError("Missing destination directory value")
    if src:
        if os.path.isabs(src):
            if os.path.exists(src):
                if os.path.isdir(src):
                    print("Source directory is available to copy")
    if dst:
        if os.path.isabs(src):
            if os.path.exists(src):
                if os.path.isdir(src):
                    print("Destination directory is available to copy")
        else:
            print("The destination directory has to be created")
            try:
                os.mkdir(dst)
            except IOError, e:
                print ("Error : %s while creating a directory %s " % (dst, e))
            print("Destination directory %s has been created to backup" % dst)


def main():
    src = ""
    dst = ""
    print("Number of input arguments : ", len(sys.argv))
    try:
        myopts, args = getopt.getopt(sys.argv[1:], "s:d:")
    except getopt.GetoptError as ex:
        print(str(ex))
        print("Usage: %s -i <source_dir> -o <destination_dir>" % sys.argv[0])
        sys.exit(2)

    for o, a in myopts:
        if o == '-s':
            src = a
        elif o == '-d':
            dst = a
        else:
            print("Usage: %s -s source -o destination" % sys.argv[0])
    src = str(src)
    dst = str(dst)

    print ("Input file : %s and output file: %s" % (src, dst))
    backup_db2_installation(src, dst)


#### Call to main() ####
if __name__ == '__main__':
    try:
        main()
    except StandardError as e:
        print(e.args)
