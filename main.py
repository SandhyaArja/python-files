def count(the_list):
    count_1=0
    for i in the_list:
        count_1+=1
    return (count_1)

#sort
def sort_n(the_list):
    count= 0
    for i in the_list:
        count+=1
    for i in range(count):
        for l in range(i+1, count):
            if the_list[i] > the_list[l]:
                the_list[i], the_list[l] = the_list[l],the_list[i]
    x=the_list
    return (x)
# MIN
def min_n(the_list):
    min_N = the_list[0]
    count = 0
    for i in the_list:
        count += 1
    for i in range(count):
        if the_list[i] < min_N:
            min_N = the_list[i]
    return (min_N)
# max
def max_n(the_list):
    max_N = the_list[0]
    count = 0
    for i in the_list:
        count += 1
    for i in range(count):
        if the_list[i] > max_N:
            max_N = the_list[i]
    return (max_N)

# index
def index_n(the_list):
    number = 1
    return (the_list[number])
# sum
def sum_list(the_list):
    sum_N = 0
    for i in the_list:
        sum_N += int(i)
    return  sum_N

# average
def average(the_list):
    sum_N = 0
    for i in the_list:
        sum_N += int(i)
    count = 0
    for i in the_list:
        count += 1
    return (sum_N/count)
the_list=list(map(int,input().split()))

print("*count","list","sum","min","max","index","sum","Average","exit")

while (True):
    list_operations=input()
    if list_operations=="exit":
        break
    else:

       dict_operatons={"count":count(the_list),"list":sort_n(the_list),"min":min_n(the_list),"max":max_n(the_list),"Index":index_n(the_list),"sum":sum_list(the_list),"Average":average(the_list)}

       if list_operations in dict_operatons :
           print(dict_operatons[list_operations])


