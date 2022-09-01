set_a = {4, 2, 8}
set_b = {1, 2}
union = set_a | set_b
print(union)
set_a = {4, 2, 8}
list_a = [1, 2]
intersection = set_a.intersection(list_a)
print(intersection)
set_a = {4, 2, 8}
tuple_a = (1, 2)
diff = set_a.difference(tuple_a)
print(diff)
set_a = {4, 2, 8}
set_b = {1, 2}
diff = set_a.symmetric_difference(set_b)
print(diff)
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_subset = set_2.issubset(set_1)
print(is_subset)
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_subset = set_2.issubset(set_1)
print(is_subset)
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_subset = set_2.issubset(set_1)
print(is_subset)
set_a = {1, 2}
set_b = {3, 4}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)
