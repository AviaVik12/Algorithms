from collections import Counter
import time
import random


def bubble_sort(arr):
    n = len(arr)
    for v in range(0, n-1):
        for d in range(v+1, n):
            if arr[v] > arr[d]:
                arr[v], arr[d] = arr[d], arr[v]


def quick_sort(arr):
    arr.sort()


def counting_sort(arr):
    counter = Counter(arr)
    res = []
    for item in range(0, 5):
        for _ in range(counter[item]):
            res.append(item)
    arr[:] = res


arr = [random.randint(0, 1000) for _ in range(10_000)]

start = time.time()
bubble_sort(arr.copy())
end = time.time()
print(f'Bubble sort result: {end - start}')

start = time.time()
counting_sort(arr.copy())
end = time.time()
print(f'Counting sort result: {end - start}')

start = time.time()
quick_sort(arr.copy())
end = time.time()
print(f'Quick sort result: {end - start}')


