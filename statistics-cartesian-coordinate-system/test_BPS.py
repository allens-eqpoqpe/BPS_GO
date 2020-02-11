class Idea_Machine():
    def __init__(self, master=None):
        self.master = master
        self.list_x =[]
        self.list_y =[]
        self.list_z =[]
        self.sorting_algorithm()
        
    def sorting_algorithm(self):
        from graphics_library import cartesian
        from support_symbol import text00, text01, text02,text03, text04, text05
        list00 =[1,2,3]
        list01 =[6,7,8]
        #for developer
        print("!!Executed: ",len(list00),len(list01))
        if len(list00) ==len(list01):
        #building list_x
            for i in range(1):
                if (list00[0] >list01[0]):
                    n =list01[0]
                    self.list_x.append(n)
                    while n <list00[0]:
                        n +=1
                        self.list_x.append(n)

                elif (list00[0] <list01[0]):
                    n =list00[0]
                    self.list_x.append(n)
                    while n <list01[0]:
                        n +=1
                        self.list_x.append(n)
                elif (list00[0] ==list01[0]):
                    self.list_x =[list00[0]]
        #building list_y
            for i in range(1):
                if (list00[1] >list01[1]):
                    n =list01[1]
                    self.list_y.append(n)
                    while n <list00[1]:
                        n +=1
                        self.list_y.append(n)

                elif (list00[1] <list01[1]):
                    n =list00[1]
                    self.list_y.append(n)
                    while n <list01[1]:
                        n +=1
                        self.list_y.append(n)
                elif (list00[1] ==list01[1]):
                    self.list_y =[list00[1]]
        #building list_z
            for i in range(1):
                if (list00[2] >list01[2]):
                    n =list01[2]
                    self.list_z.append(n)
                    while n <list00[2]:
                        n +=1
                        self.list_z.append(n)

                elif (list00[2] <list01[2]):
                    n =list00[2]
                    self.list_z.append(n)
                    while n <list01[2]:
                        n +=1
                        self.list_z.append(n)
                elif (list00[2] ==list01[2]):
                    self.list_z =[list00[2]]
            #for developer
            print("###############")
            print("list_x =",self.list_x)
            print("list_y =",self.list_y)
            print("list_z =",self.list_z)
            self.distributed()
            print(text05*10)
            cartesian(len(self.list_y))

    def distributed(self):
        for i in self.list_y:
            for j in self.list_x:
                print("({},{})".format(i,j),end=" ")
            print()
    def statistics(self):
        
        pass

A =Idea_Machine("ryan")