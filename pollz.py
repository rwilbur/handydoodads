import subprocess
import sys
import os
import requests
from bs4 import BeautifulSoup
import sys, traceback
#import Queue
import threading
import time

#exitFlag = 0
#class voteThreading(threading.Thread):
    
    #def __init__(self, threadID):
        #threading.Thread.__init__(self, vote)
        #self.threadID = threadID
    #def run(self):
        #print "Starting " + self.name
        #vote(self.name, self.q)
        #print "Exiting " + self.name
    
    
#def process_data(threadName, vote):
    #while not exitFlag:
        #queueLock.acquire()
        #if not workQueue.empty():
            #data = q.get()
            #queueLock.release()
            #print "%s processing %s" % (threadName, data)
        #else:
            #queueLock.release()
        #time.sleep(1)
    
#threadList = ["Thread-1", "Thread-2", "Thread-3"]
#nameList = ["One", "Two", "Three", "Four", "Five"]
#queueLock = threading.Lock()
#workQueue = Queue.Queue(10)
#threads = []
#threadID = 1

## Create new threads
#for tName in threadList:
    #thread = myThread(threadID, tName, workQueue)
    #thread.start()
    #threads.append(thread)
    #threadID += 1

## Fill the queue
#queueLock.acquire()
#for word in nameList:
    #workQueue.put(word)
#queueLock.release()

## Wait for queue to empty
#while not workQueue.empty():
    #pass

## Notify threads it's time to exit
#exitFlag = 1

## Wait for all threads to complete
#for t in threads:
    #t.join()
#print "Exiting Main Thread"    
    
    
    
    

def main():
    try:
        print("\n\n\n\n\n")
        n_votes = "";
        text = requests.get('https://www.uvm.edu/~slife/portal/poll/poll.php?vote').text
        soup = BeautifulSoup(text, 'html.parser')

        tableContents = soup.find(class_='button-holder').contents[1].contents

        for i in range(1, 8, 2):
            n = int(i/2+.5)
            print(n, "\b: ", tableContents[i].find('td').text.strip())
        sel = input()
        url = "https://www.uvm.edu/~slife/portal/poll/poll.php?vote="+sel
        n_votes = input ("How many votes? (-1 for infinity): ")
        wtime = input ("How long to wait between votes(in seconds)? (0 for as fast as possible): ")
        if eval(n_votes) < 0:
            n_votes = 0;
            while(True):
                subprocess.run(["curl",url, "-s"], stdout=subprocess.PIPE)
                n_votes += 1;
                time.sleep(eval(wtime))
        else:
            for x in range(0, eval(n_votes)):
                subprocess.run(["curl", url,"-s"], stdout=subprocess.PIPE)
                time.sleep(eval(wtime))
            print("\nThank you for your voting \033[92m"+ str(n_votes)+"\033[0m times, have a nice day!")

    except KeyboardInterrupt:
        print("\nThank you for your voting \033[92m"+ str(n_votes)+"\033[0m times, have a nice day!\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()

