from collections import Counter


def counting_sort(arr):
    counter = Counter(arr)
    res = []
    for item in range(0, 5):
        for _ in range(counter[item]):
            res.append(item)
    arr[:] = res


arr = [2, 3, 1, 4, 0]
counting_sort(arr)
print(arr)




