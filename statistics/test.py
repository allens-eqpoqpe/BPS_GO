'''
import math
A =[]
B =[]
place_data = float(input('yours'))
print(type(place_data))
print(int(place_data))
print(math.ceil(place_data))
'''
'''
gr =input('yours')
print(type(gr))
print(type(int(gr)),int(gr))
'''
'''
import re

gr ='(12312,125152)'
Ki =re.findall(r'\d+\.?\d*',gr)
a =Ki[0]
b =Ki[1]
print(int(a) +int(b),'({},{})'.format(a,b))
'''
'''
list00 =[123123.213,124124.0]
list01 =[]
it =iter(list00)
for i in it:
    if i -int(i) ==0:
        i =int(i)
        print(list00.index(i))
        list00[list00.index(i)] =i
    else:
        i =i
    print(list00)
'''
'''
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

sleep(.7)
'''
'''
string ="DATA ERROR"
print(" "*3,"#"*(len(string) +3) +"#")
for i in range(1):
    print(" "*3,"#"+"!"*(len(string) +2) +"#")
for i in range(1):
    print(" "*3,"#!" +string +"!#")
for i in range(1):
    print(" "*3,"#"+"!"*(len(string) +2) +"#")
print(" "*3,"#"*(len(string) +3) +"#")


list00 =[10]
list01 =[1]
list_x =[]
n =list01[0]
while n <list00[0]:
    n +=1
    list_x.append(n)
    print(list_x)

for i in range(2):
    print("yes")
'''
'''
    if len(list00) ==len(list01):
        for i in range(len(list00)):
            #building list_x
            if (list00[0] >list01[0]):
                n =list01[0]
                while n <list00[0]:
                    n +=1
                    list_x.append(n)

            elif (list00[0] <list01[1]):
                n =list01[0]
                while n <list00[0]:
                    n +=1
                    list_x.append(n)

            elif (list00[0] ==list01[1]):
                list_x[0] =list00[0] or list01[0]
            #building list_y
            if (list00[1] >list01[1]):
                n =list01[0]
                while n <list00[0]:
                    n +=1
                    list_x.append(n)

                elif (list00[1] <list01[1]):
                    n =list01[0]
                    while n <list00[0]:
                        n +=1
                        list_x.append(n)

                elif (list00[1] ==list01[1]):
                    list_y[0] =list00[1] or list01[1]
                #building list_z
                elif (list00[2] >list01[2]):
                    n =list01[0]
                    while n <list00[0]:
                        n +=1
                        list_x.append(n)

                elif (list00[2] <list01[2]):
                    n =list01[0]
                    while n <list00[0]:
                        n +=1
                        list_x.append(n)

                elif (list00[2] ==list01[2]):
                    list_z[0] =list00[2] or list01[2]
                print(list_x,list_y,list_z)
'''
'''
list00 =[1.0,2.0,3.0]
list01 =[2.0,5.0,7.0]
list_x =[]
list_y =[]
list_z =[]
for i in range(1):
########################                #building list_x
    if (list00[0] >list01[0]):
        n =0
        while n <3:
            n +=1
            print("one")

    elif (list00[0] <list01[0]):
        n =0
        while n <3:
            n +=1
            print("two")
########################                 #building list_y
for i in range(1):
    if (list00[1] >list01[1]):
        n =0
        while n <3:
            n +=1
            print("one")

    elif (list00[1] <list01[1]):
        n =0
        while n <3:
            n +=1
            print("two")
########################                 #building list_z
for i in range(1):
    if (list00[2] >list01[2]):  
        n =0
        while n <3:
            n +=1
            print("one")
    elif (list00[2] <list01[2]):
        n =0
        while n <3:
            n +=1
            print("two")
'''
for i in range(1):
    print(i)