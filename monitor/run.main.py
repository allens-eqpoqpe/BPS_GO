from urllib.request import urlopen
import os, sys, re, time
from time import sleep

n =0
t =0
while True:

    t1 =time.time()
    html =urlopen('https://github.com').read().decode('utf-8')
    t2 =time.time()
    n +=1
    t +=(t2 -t1)

    if re.match("Recent activity",html) is True:
        print('y')
        break
    
    print("view few: %d"%n,"time: {:.4} Sec".format(t2 -t1))
    if n ==5:

        print("every: {}".format(t/5))
        break