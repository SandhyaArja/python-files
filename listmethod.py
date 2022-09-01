#list add method append
def list_append(n):
        list_s=[]
        for i in n:
            list_s.append(int(i))
            list_s.append(s)
        return list_s
#list count
def list_count(n):
        count=0
        for i in n:
            count+=1
        return count
#list extend will add two lists
def list_extend(n,m):
    list_n = n.extend(m)
    return list_n
#list insert will help that to add new elements in list
def list_insert(n):
    list_n=n.insert(s)
    return list_n
# pop method will remove the last method in the given list
def list_pop(n):
    list_n=n.pop()
    return list_n
# clear method  will clear the entire list
def list_clear(n):
    list_clear=n.clear()
    return list_clear
# remove method will remove particular digit in given list
def list_remove(n,s):
    list_remove=n.remove(s)
    return list_remove
# index method will helpus to at the given index what element is located
def list_index(n):
    list_index=n.index(s)
    return list_index
# count method will help to count the given elements in the list
def list_count(n):
    list_count=n.count(s)
    return list_count
# sort method will sortthe list and return it in an ascending order
def sort_list(n,m):
    list_sort=n,m.sort()
    return list_sort
# sorted method will help us to create a new sorted list
def sorted_list(n):
    list_sorted=sorted(n)
    return list_sorted
#reverse method will reverse the list
def list_reverse(n):
    list_rev=sorted(n,reverse=True)
    return list_rev
# copy method will copy the list and returns the new copy of the given list
def list_copy(n):
    list_copy=n.copy()
    return list_copy

    


n=list(map(int,input().split()))
m=list(map(int,input().split()))
s=int(input())
print("*append","*count","*copy","*reverse","*sorted","*sort","*index","*remove","*clear","*pop","*extend","*insert")
while True:
    list_methods=input()
    list_operations={"append":list_append(n),"count":list_count(n),"copy":list_copy(n),"reverse":list_reverse(n),"sort":sort_list(n,m),"sorted":sorted_list(n),"index":list_index(n)
                     ,"remove":list_remove(n),"clear":list_clear(n),"pop":list_pop(n),"extend":list_extend(n,m),"insert":list_insert(n)}
    if list_methods in list_operations:
        print(list_operations[list_methods])
