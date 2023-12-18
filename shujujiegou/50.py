class Solution:
    def firstUniqChar(self, s):
        if s == '':
            return ' '
        else:

            i = 0
            for i in range(len(s)):
                j = 0
                for n in range(len(s)):
                    if s[i] == s[n]:
                        j = j + 1
                    else:
                        pass
                if j == 1:
                    return s[i]
                elif i == len(s)-1 and j != 1:
                    return " "

c = Solution()
c.firstUniqChar("cca")


