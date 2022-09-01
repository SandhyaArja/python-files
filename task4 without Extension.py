list_N = input().split(",")

count = 0
for i in list_N:
    count += 1
print("count:", count)
# sort
for i in range(count):
    for l in range(i, count):
        if list_N[i] > list_N[l]:
            list_N[i], list_N[l] = list_N[l], list_N[i]
print(list_N)
# MIN
min_N = list_N[0]
for i in range(count):
    if list_N[i] < min_N:
        min_N = list_N[i]
print("min_num:", min_N)
# max
max_N = list_N[0]
for i in range(count):
    if list_N[i] > max_N:
        max_N = list_N[i]
print("min_num:", max_N)

# index
number = 1
print("Index:", list_N[number])
# sum
sum_N = 0
for i in list_N:
    sum_N += int(i)
print("sum:", sum_N)
# average
print("Average:", sum_N / count)