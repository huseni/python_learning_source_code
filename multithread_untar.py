__author__ = 'kathiria'

from multiprocessing.pool import ThreadPool, Pool
import StringIO
import tarfile


def write_tar():
    tar = tarfile.open('test.tar', 'w')
    contents = 'line1'
    info = tarfile.TarInfo('file1.txt')
    info.size = len(contents)
    tar.addfile(info, StringIO.StringIO(contents))
    tar.close()


def test_multithread():
    tar   = tarfile.open('test.tar')
    files = [tar.extractfile(member) for member in tar.getmembers()]
    pool  = ThreadPool(processes=1)
    pool.map(read_file, files)
    tar.close()


def test_multiproc():
    tar   = tarfile.open('test.tar')
    files = [tar.extractfile(member) for member in tar.getmembers()]
    pool  = Pool(processes=1)
    pool.map(read_file, files)
    tar.close()


def read_file(f):
    print f.read()

#write_tar()
test_multithread()
test_multiproc()
