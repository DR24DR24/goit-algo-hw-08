import random
import heapq

CabelNumbers=10

cabels=[random.randint(0,CabelNumbers) for _ in range(CabelNumbers)]

print(cabels)

cabels_heap=[]
for i in range(CabelNumbers):
    heapq.heappush(cabels_heap,cabels[i])

connected_cabels=[]
s=0
while len(cabels_heap)>1:
    next_cabel1=heapq.heappop(cabels_heap)
    next_cabel2=heapq.heappop(cabels_heap)
    cost=next_cabel1+next_cabel2
    heapq.heappush(cabels_heap,cost)
    s+=cost
    connected_cabels.append((next_cabel1,next_cabel2))

print(f"connected_cabels: {connected_cabels}, connection cost: {s}")    