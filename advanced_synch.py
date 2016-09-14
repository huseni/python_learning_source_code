__author__ = 'kathiria'

import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print ("Finished Background file write to " + self.out)

def main():
    message1 = input("Enter a string to store: ")
    message2 = input("Enter a number to store: ")
    background1 = AsyncWrite (message1, 'out.txt')
    background2 = AsyncWrite (message2, 'out.txt')
    background1.start()
    background2.start()
    print ("The program can continue to run while it write in another thread")
    print( 100 + 400)
    background1.join() # Wait until the thread is finish
    background2.join()
    print ("Waited until the thread was complete")
    print ("Main complete")


if __name__ == '__main__':
    main()


