##################
#Global variables#
##################
list_x =[2,3,4,5,6,7]
list_y =[5,6,7,8,9]
#####for test#####
###sort total list

total_value =[]
def sroting():

    total_value.append(len(list_x))
    total_value.append(len(list_y))
    if total_value[0] >total_value[1]:
        from support_class import support_sorting
        support_sorting(1,0)
    else:
        if total_value[0] <total_value[1]:
            from support_class import support
            support_sorting(0,1)
        elif total_value[0] ==total_value[1]:
            from support_class import support
            support_sorting(1,0)

sroting()