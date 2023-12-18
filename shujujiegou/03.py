# class Solution:
#     def findRepeatNumber(self, nums):
#         for i in range(len(nums)):
#             for n in range(i+1, len(nums)):
#                 if nums[i] == nums[i+n]:
#                     return nums[i]

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = []
        for num in nums:
            if num in dic:
                return num
            dic.append(num)
        return -1



c = Solution()
print(c.findRepeatNumber([2, 3, 1, 0, 2]))