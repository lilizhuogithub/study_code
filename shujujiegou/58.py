# class Solution:
#     def reverseLeftWords(self, s: str, n: int) -> str:
#         res1 = []
#         res2 = []
#         for i in range(n):
#             res1.append(s[i])
#         for i in range(len(s)-n):
#             res2.append(s[i+n])
#         return "".join(res2+res1)

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)


c = Solution()
print(c.reverseLeftWords("abcdefg", 2))

'''
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)


'''
