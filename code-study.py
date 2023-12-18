# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         p = 0
#         q = 1
#         while q < len(nums):
#             if nums[p] == nums[q]:
#                 q+=1
#             else:
#                 nums[p+1] = nums[q]
#                 p+=1
#                 q+=1
#         return p
#         # print(B)
    
# #test
# nums = [1,1,2]
# print(Solution().removeDuplicates(nums))
# nums = [0,0,1,1,1,2,2,3,3,4]
# print(Solution().removeDuplicates(nums))


#只出现一次的数字
#利用哈希表，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def singleNumber(self, nums):
        map = {}
        for i in nums:
            count = map.get(i)
            count = count+1 if count is not None else 1
            map[i] = count
        for i in map.keys():
            count = map.get(i)
            if count == 1:
                return i
        return -1	#没有只出现一个的数字  

#验证SingleNumber算法
nums = [4,1,2,1,2,4,5]
print(Solution().singleNumber(nums))


