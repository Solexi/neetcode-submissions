class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        numbers = Counter(nums)
        res = []

        for item in numbers.most_common(k):
            # print(item)
            res.append(item[0])
        return res


        # print(res)