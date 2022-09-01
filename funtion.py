def count(the_list):
        c=0
        for i in the_list:
            c+=1
        return (c)
def list_n(the_list):
    for i in range(len(the_list)):
        for j in range(i+1,len(the_list)):
            if the_list[i]>the_list[j]:
                the_list[i],the_list[j]=the_list[j],the_list[i]
    x=the_list
    return(x)
def min_n(the_list):
   num=1000000000
   for i in the_list:
       if i<num:
           num=i
   return(num)
def max_n(the_list):
    num = 1000000000
    for i in the_list:
        if i > num:
            num = i
    return(num)
def index_n(the_list):
    num_n=4
    return(the_list[num_n])
def sum_n(the_list):
    c=0
    for i in the_list:
        c+=i
    return(c)
def average(the_list):
    c=0
    for i in the_list:
        c=+i
    return(c/len(the_list))
the_list=list(map(int,input().split()))
while (True):
    l=[]
    list_operations=input()
    if list_operations=="exit":
        break
    else:
       l.append(list_operations)
       dict_operatons={"count":count(the_list),"list":list_n(the_list),"min":min_n(the_list),"max":max_n(the_list),"Index":index_n(the_list),"sum":sum_n(the_list),"Average":average(the_list)}
       for i in l:
           print(dict_operatons[i])