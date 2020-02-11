from support_class import MAPS_place
from support_class import Idea_Machine
from graphics_library import Graphics
from random import randint
import re,os,sys

Graphics.tree

print('# '*19)
rnd2 =randint(1,19)
for x in range(1,15):
	rnd1 =randint(1,rnd2)
	if x==1:
		ch ='$'
	elif rnd1%4==0:
		ch ='o'
	elif rnd1%3==0:
		ch ='i'
	else:
		ch ='*'
	print('#','{:^33}'.format(ch*x),'#')
print('# '*19)

list00 =[]
list01 =[]

cake0 =input('name: ')
cake1 =input('Place: ')
#list =[]
#list =[re.finditer(r'\d+',cake1)]

list =[]
it =re.finditer(r"\d+",cake1)
for match in it:
	print(match.group())
	gr =type(match.group())
	list.append(gr((match.group())))
A1 =MAPS_place(cake0,cake1)

print(A1.name,A1.place)

cake0 =input('name: ')
cake1 =input('Place: ')
list =[]
list =re.finditer(r'd+',cake1)
B1 =MAPS_place(cake0,cake1)

print(B1.name,B1.place)

(Te01) =list01[0]
Te11 =list01[1]
(Te00) =list00[0]
Te10 =list00[1]

T ='list00 =' +'[{},{}]'.format(Te00,Te01)
f =open('/home/ryan/Public/BPS/statistics/support_library.py','w')
f.write(T)
T ='\nlist01 =' +'[{},{}]'.format(Te01,Te11)
f =open('/home/ryan/Public/BPS/statistics/support_library.py','a')
f.write(T)
f.close()

Idea_Machine.idea_chose()
Idea_Machine.action()