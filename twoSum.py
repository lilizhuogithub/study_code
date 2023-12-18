from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for index, num in enumerate(nums):
            cur = target - num
            if num in temp:     # 
                return temp[num], index
            temp[cur] = index
        

# 测试用例
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)
