class Solution:
    def missingNumber(self, nums):
        a = []
        for i in range(len(nums)+1):
            a.append(i)
            if i in nums:
                a.remove(i)
            else:
                return i


# class Solution:
#     def missingNumber(self, nums):
#         i, j = 0, len(nums) - 1
#         while i <= j:
#             m = (i + j) // 2
#             if nums[m] == m: i = m + 1
#             else: j = m - 1
#         return i




c = Solution()
print(c.missingNumber([1]))

