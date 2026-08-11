class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, v in count.items():
            freq[v].append(i)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res