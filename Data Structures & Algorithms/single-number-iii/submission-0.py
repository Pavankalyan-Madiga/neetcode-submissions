class Solution:

    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        result=[]

        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] == 1:
                result.append(num)
        return result