class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                       # notebook: number -> its position
        for i in range(len(nums)):
            partner = target - nums[i]  # the number I need to complete the pair
            if partner in seen:         # did I already see it?
                return [seen[partner], i]
            seen[nums[i]] = i           # no: write my number and position