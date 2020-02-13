class MAPS_USER:
    name ="None"
    place =0,0,0
    def __init__(self,user_name,user_place):

        self.name ="User: " +user_name
        self.place ="Place: " +user_place

list_x =[]
list_y =[]
list_z =[]
class Idea_Machine(MAPS_USER):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.list_x =[]
        self.list_y =[]
        self.list_z =[]
        self.sorting()
        self.distributed()
        
    def sorting(self):
        from library import list00, list01
        from graphics_library_support import cartesian
        from symbol_support import text00, text01, text02,text03, text04, text05
        #for developer
        print("!!Executed: ",len(list00),len(list01))
        if len(list00) ==len(list01):
            value =0
            for get_list in (self.list_x, self.list_y, self.list_z):
                if (list00[value] >list01[value]):
                    n =list01[value]
                    get_list.append(n)
                    print(n)
                    while n <list00[value]:
                        n +=1
                        get_list.append(n)

                elif (list00[value] <list01[value]):
                    n =list00[value]
                    get_list.append(n)
                    print(n)
                    while n <list01[value]:
                        n +=1
                        get_list.append(n)
                elif (list00[value] ==list01[value]):
                    get_list =[list00[value]]
                value +=1
        else:
            string ="DATA ERROR"
            print(" "*3,"#"*(len(string) +3) +"#")
            for i in range(1):
                print(" "*3,"#"+"!"*(len(string) +2) +"#")
            for i in range(1):
                print(" "*3,"#!" +string +"!#")
            for i in range(1):
                print(" "*3,"#"+"!"*(len(string) +2) +"#")
            print(" "*3,"#"*(len(string) +3) +"#")       
            
        #for developer
        print("###############")
        print("list_x =",self.list_x)
        print("list_y =",self.list_y)
        print("list_z =",self.list_z)

    def distributed(self):
        for i in self.list_y:
            for j in self.list_x:
                print("({},{})".format(i,j),end=" ")
            print()