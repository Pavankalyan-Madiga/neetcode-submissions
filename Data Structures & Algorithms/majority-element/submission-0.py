class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n // 2

        dic = {}

        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1

            if dic[num] > majority:
                return num
        