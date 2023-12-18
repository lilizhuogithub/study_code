class Solution:
    def replaceSpace(self, s: str) -> str:
        b = s.replace(" ", "%20")
        return b


c = Solution()
print(c.replaceSpace("We are happy."))


'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)

'''

