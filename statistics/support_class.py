class MAPS_place:

    left = '-'
    right ='+'
    up ='-'
    down ='+'
    #can help you to calculate and get the easiest way
    def __init__(self,user_name,user_data):
        self.name ='UESR: ' +user_name
        self.place ='Place: ' +'({})'.format(user_data)
    def __str__(self):
        return 
    
    #S
    def move_add(self,more):
        import re
        gr =self.place
        Ki =re.findall(r'\d+\.?\d*',gr)
        a1 =float(Ki[0]) +more
        b1 =float(Ki[1]) +more

        list00 =[]
        list00.append(a1)
        list00.append(b1)
        it =iter(list00)
        for i in it:
            if i -int(i) ==0:
                i =int(i)
                list00[list00.index(i)] =i
            else:
                i =i
        print(i,end=' ')
        self.place ='{},{}'.format(list00[0],list00[1])

    def move_reduce(self):
        import re
        gr =self.place
        Ki =re.findall(r'\d+\.?\d*',gr)

        a1 =float(Ki[0]) -more
        b1 =float(Ki[1]) -more

        list00 =[]
        list00.append(a1)
        list00.append(b1)
        it =iter(list00)
        for i in it:
            if i -int(i) ==0:
                i =int(i)
                list00[list00.index(i)] =i
            else:
                i =i
        print(i,end=' ')
        self.place ='{},{}'.format(list00[0],list00[1])


#
list_x =[]
list_y =[]

class Idea_Machine:
    
    
    #about lift right up down
    def idea_chose():
        
        from support_library import list00
        from support_library import list01
        #get vol
        if (list00[0] <list01[0]) and (list00[1] <list01[1]):
            for i in range(list00[0],list01[0]):
                list_x.append(i)
            list_x.append(list01[0])
            for i in range(list00[1],list01[1]):
                list_y.append(i)
            list_y.append(list01[1])

        elif (list00[0] <list01[0]) and (list00[1] >list01[1]):
            for i in range(list00[0],list01[0]):
                list_x.append(i)
            list_x.append(list01[0])
            for i in range(list01[1],list00[1]):
                list_y.append(i)
            list_y.append(list00[1])

        elif (list00[0] <list01[0]) and (list00[1] ==list01[1]):
            for i in range(list00[0],list01[0]):
                list_x.append(i)
            list_x.append(list01[0])
            for i in range(list00):
                list_y.append(i)
            list_y.remove(0)
            list_y.append(list00[1])

        elif (list00[0] >list01[0]) and (list00[1] <list01[1]):
            for i in range(list01[0],list00[0]):
                list_x.append(i)
            list_x.append(list00[0])
            for i in range(list00[1],list01[1]):
                list_y.append(i)
            list_y.append(list01[1])
            
        elif (list00[0] >list01[0]) and (list00[1] >list01[1]):
            for i in range(list01[0],list00[0]):
                list_x.append(i)
            list_x.append(list01[0])
            for i in range(list01[1],list00[1]):
                list_y.append(i)
            list_y.append(list00[1])

        elif (list00[0] >list01[0]) and (list00[1] ==list01[1]):
            for i in range(list01[0],list00[0]):
                list_x.append(i)
            list_x.append(list01[0])
            for i in range(list00):
                list_y.append(i)
            list00.remove(0)
            list_y.append(list00[1])

        elif (list00[0] ==list01[0]) and (list00[1] <list01[1]):
            for i in range(list00[0]):
                list_x.append(i)
            list_x.append(list00[0])
            list_x.remove(0)
            for i in range(list00[1],list01[1]):
                list_y.append(i)
            list_y.append(list01[1])

        elif (list00[0] ==list01[0]) and (list00[1] >list01[1]):
            for i in range(list00[0]):
                list_x.append(i)
            list_x.append(list00[0])
            list_x.remove(0)
            for i in range(list01[1]),list00[1]:
                list_y.append(i)
            list_y.append(list00[1])

    def action():

        print("#"*20)
        n =0
        for i in range(list_y[0],list_y[(len(list_y)-1)]+1):
            for j in range(list_x[0],list_x[(len(list_x)-1)]+1):
                #all group build a new list
                n +=1
                list_n =[i,j]
                print("V {}".format(n),list_n)
'''
        print("#"*20)
        n =0
        for i in (list_y[0],list[len(list_y)-1]):
            for j in (list_x[0],list[len(list_x)-1]):
                n +=1
                vl_n =[i,j]
                print("V {}".format(n),vl_n)
'''