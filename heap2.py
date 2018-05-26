from heapq import heappop, heappush, heapify

heap = []
nums = [12, 3, -2, 314, -234, 0, 100, 3]

for x in nums:
  heappush(heap, x) # make MIN heap

# print down - up elements
while heap:
  print(heappop(heap)) # get root

# make correct min heap from array
nums2 = [23, 3, 4, 5, -2, -33, 233, 100, 20, -55]

heapify(nums2) # make min heap

print(nums2)