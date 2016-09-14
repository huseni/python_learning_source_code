__author__ = 'kathiria'

import multiprocessing


def foo():
    print "this is foo process"


if __name__ == '__main__':
    for i in range(4):
        jobs = list()
        print("starting the parallel processing ...", i)
        m = multiprocessing.Process(target=foo, name="This is a food method")
        jobs.append(m)
        m.start()
        m.join()
        print("All processes are now completed !")


