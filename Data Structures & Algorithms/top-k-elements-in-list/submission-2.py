class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums = Counter(nums)
        res = []

        for item in nums.most_common(k):
            # print(item)
            res.append(item[0])
        return res


        # print(res)