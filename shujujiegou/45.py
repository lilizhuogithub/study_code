from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l, r):
            if l >= r: return   # 终止条件，区间只有一个元素，或者为空，无需排序
            i, j = l, r     # 双指针
            while i < j:    # 递推
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1  # 从右向左遍历，找到第一个满足strs[j] + strs[l] < strs[l] + strs[j]的位置
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1  # 从左向右遍历，找到第一个满足strs[i] + strs[l] > strs[l] + strs[i]的位置
                strs[i], strs[j] = strs[j], strs[i]   # 如果i < j，交换strs[i]和strs[j]
            strs[i], strs[l] = strs[l], strs[i] # 将枢轴元素放置在正确的位置上
            quick_sort(l, i - 1)     # 对枢轴元素左边的子数组 [l, i-1]递归
            quick_sort(i + 1, r)    # 对枢轴元素右边的子数组 [i+1, r]递归

        strs = [str(num) for num in nums]   # 转换成字符串
        quick_sort(0, len(strs) - 1)    # 排序
        return ''.join(strs)    # 拼接


c = Solution()
print(c.minNumber([10, 2, 1]))
