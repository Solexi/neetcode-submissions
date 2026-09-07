class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i in nums:
            if i in count:
                return True
            count[i] += 1

        return any(value == 2 for value in count.values())