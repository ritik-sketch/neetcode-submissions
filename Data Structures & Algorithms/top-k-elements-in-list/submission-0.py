class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x in count:
                count[x] = count[x] + 1
            else:
                count[x] = 1
        order = sorted(count, key=count.get, reverse=True)
        return order[:k]