import heapq

def merge_k_lists(lists):
    out=[]
    heap=[]
    for i,item in enumerate(lists):
        if item:
            heapq.heappush(heap,(-item.pop(),i))
    while heap:
        item,i=heapq.heappop(heap)
        out.append(-item)
        if lists[i]:
            heapq.heappush(heap,(-lists[i].pop(),i))
    out.reverse()
    return out

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)