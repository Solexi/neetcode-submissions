class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        currSum = 0
        left, right = 0, len(nums)-1

        seen = {}

        for index, num in enumerate(nums):
            diff = target - nums[index]

            if diff in seen:
                return [seen[diff], index]
            seen[num] = index

        # while left < right:
        #     sums = nums[left] + nums[right]

        #     if sums == target:
        #         return [left, right]
        #     elif sums > target:
        #         right -= 1
        #     elif sums < target:
        #         left += 1
        #     else:
        #         return [left, right]
        