def common_elements(list1,list2):
    newlist = []
    for i in list1:
        if i in list2:
            newlist.append(i)
    print(newlist)
 

list1=[2,3,4]
list2=[5,6,2]
common_elements(list1,list2)