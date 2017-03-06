import subprocess
import sys
import os
import requests
from bs4 import BeautifulSoup
import sys, traceback
import threading
import time

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

