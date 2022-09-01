# list add method append
def list_append(n, num):
    n.append(num)
    return n


# list count
def list_count(n):
    count = 0
    for i in n:
        count += 1
    return count


# list extend will add two lists
def list_extend(n, m):
    list_n = n.extend(m)
    return list_n


# list insert will help that to add new elements in list
def list_insert(n, num):
    list_n = n.insert(num)
    return list_n


# pop method will remove the last method in the given list
def list_pop(n):
    n.pop()
    return n


# clear method  will clear the entire list
def list_clear(n):
    list_clear = n.clear()
    return list_clear


# remove method will remove particular digit in given list
def list_remove(n, num):
    list_remove = n.remove(num)
    return list_remove


# index method will helpus to at the given index what element is located
def list_index(n, num):
    list_index = n.index(num)
    return list_index


# count method will help to count the given elements in the list
# def list_count(n):
#   list_count=n.count(num)
#   return list_count
# sort method will sortthe list and return it in an ascending order
# def sort_list(n,m):
#   list_sort=n,m.sort()
#  return list_sort
# sorted method will help us to create a new sorted list
def sorted_list(n):
    list_sorted = sorted(n)
    return list_sorted


# reverse method will reverse the list
def list_reverse(n):
    list_rev = sorted(n, reverse=True)
    return list_rev


# copy method will copy the list and returns the new copy of the given list
def list_copy(n):
    list_copy = n.copy()
    return list_copy


input_num_list = input().split()
n = []
for i in input_num_list:
    n.append(int(i))

print("*append", "*count", "*copy", "*reverse", "*sorted", "*sort", "*index", "*remove", "*clear", "*pop", "*extend",
      "*insert")
list_methods = input()
# "sort":sort_list,
list_operations = {"append": list_append, "count": list_count, "copy": list_copy, "reverse": list_reverse,
                   "sorted": sorted_list, "index": list_index
    , "remove": list_remove, "clear": list_clear, "pop": list_pop, "extend": list_extend, "insert": list_insert}
if list_methods in list_operations:
    if list_methods == "count" or list_methods == "copy" or list_methods == "reverse" or list_methods == "sort" or list_methods == "sorted" or list_methods == "clear" or list_methods == "pop":
        result = list_operations[list_methods]
        res=result(n)
        print(res)
    elif list_methods == "append" or list_methods == "insert" or list_methods == "remove" or list_methods == "index" or list_methods == "remove":
        num = int(input())
        result = list_operations[list_methods](n, num)
        res=result()
        print(res)
    elif list_methods == "extend":
        m = input()
        result = list_operations[list_methods](n, m)
        res=result()
        print(res)
