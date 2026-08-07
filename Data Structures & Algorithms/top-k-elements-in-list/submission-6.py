class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        cnt = {}

        #count the number of occurences for each integer
        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)

        #build the list in ascending order in terms of occurrences
        for num, cnt in cnt.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            j = 0
            while j < len(freq[i]):
                if len(res) == k:
                    return res 
                res.append(freq[i][j])
                j += 1


        return res