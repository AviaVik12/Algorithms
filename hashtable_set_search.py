import pprint

arr = [1, 2, 2, 3, 4, 9, 10, 10, 12, 13, 27, 35]

my_set = set(arr)
for i in range(4, 5):
    pprint.pprint(i in my_set)
