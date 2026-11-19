class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            result = target - num

            if result in dic:
                return [dic[result], i]

            dic[num] = i