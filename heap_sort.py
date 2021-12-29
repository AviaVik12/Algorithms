import heapq

heap = [3, 5, 2, 3, 1, 8, 3]

heapq.heapify(heap)
arr = [heapq.heappop(heap) for _ in range(len(heap))]
print(heap)
print(arr)

