from random import randint
from class_support import MAPS_USER,Idea_Machine
import re,os,sys

##################
#check file value#
##################

##############
#BUILD PERSON#
##############

cake0 =input("name: ")
cake1 =input("Place: ")
person_A =MAPS_USER(cake0,cake1)
print(person_A.name,"(" +person_A.place +")")

patten =re.compile(r'\d+')
result0 =patten.findall(cake1)
list =[]
for i in range(len(result0)):
    list.append(float(result0[i]))

if len(list) <3:
    string ="list00 =[{},{}]\n".format(list[0],list[1])
    filter =open("library.py","w")
    filter.write(string)
else:
    string ="list00 =[{},{},{}]\n".format(list[0],list[1],list[2])
    filter =open("library.py","w")
    filter.write(string)

cake0 =input("name: ")
cake1 =input("Place: ")
person_B =MAPS_USER(cake0,cake1)
print(person_B.name,"(" +person_B.place +")")

patten =re.compile(r'\d+')
result0 =patten.findall(cake1)
list =[]
for i in range(len(result0)):
    list.append(float(result0[i]))

if len(list) <3:
    string ="list01 =[{},{}]".format(list[0],list[1])
    filter =open("library.py","a")
    filter.write(string)
    filter.close()
else:
    string ="list01 =[{},{},{}]".format(list[0],list[1],list[2])
    filter =open("library.py","a")
    filter.write(string)
    filter.close()