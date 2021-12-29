def bubble_sort(arr):
    n = len(arr)
    for v in range(0, n-1):
        for d in range(v+1, n):
            if arr[v] > arr[d]:
                arr[v], arr[d] = arr[d], arr[v]


arr = [2, 3, 1, 4, 0]
bubble_sort(arr)
print(arr)
