#Heap queue or heapq in python

import heapq
li = [5, 7, 9, 1, 3]
 
print("The created heap is : ", end="")
print(list(li))
heapq.heappush(li, 4)

print("The modified heap after push is : ", end="")
print(list(li))
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
