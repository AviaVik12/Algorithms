import bisect

arr = [1, 2, 2, 3, 4, 9, 10, 10, 12, 13, 27, 35]

print(bisect.bisect_left(arr, 10))
print(bisect.bisect_right(arr, 10))
print(bisect.bisect_right(arr, 0))
