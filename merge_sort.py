def merge_sort(arr) -> list:
    def merge(arr1: list, arr2: list) -> list:
        res = []
        res_cnt = len(arr1) + len(arr2)
        while len(res) < res_cnt:
            if not len(arr1):
                res += arr2
                return res
            if not len(arr2):
                res += arr1
                return res
            if arr1[0] < arr2[0]:
                res.append(arr1.pop(0))
            else:
                res.append(arr2.pop(0))
        return res
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    together = merge(arr1, arr2)
    return together


arr = [1, 3, 2, 10, 5, 55, 8]
res = merge_sort(arr)
assert res == sorted(arr)
print(res)


