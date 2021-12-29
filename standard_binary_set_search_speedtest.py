import random
import time
import bisect

arr = sorted([random.randint(0, 1000) for _ in range(10_000_000)])

# Standard search timer
start = time.time()
for i in range(0, 100):
    print(i in arr, end=' ')
end = time.time()
print('\nStandard list search time: ', end - start)

# Binary search timer
start = time.time()
for i in range(0, 100):
    ind = bisect.bisect_left(arr, i)
    print(arr[ind] == i, end=' ')
end = time.time()
print('\nBinary search time: ', end - start)

# Set search timer
my_set = set(arr)
start = time.time()
for i in range(0, 100):
    print(i in my_set, end=' ')
end = time.time()
print('\nSet search time: ', end - start)


