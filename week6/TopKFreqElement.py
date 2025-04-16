class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        heap = [(-freq,val) for val,freq in counter.items()]
        heapq.heapify(heap)
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
