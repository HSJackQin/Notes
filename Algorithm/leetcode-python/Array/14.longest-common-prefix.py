class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        index = len(strs[0])
        if len(strs) == 1:
            return strs[0][:index]
        for i in range(1,len(strs)):
            if len(strs[i]) < index:
                index = len(strs[i])
            j = 0
            while j < index:
                if strs[i][j] == strs[0][j]:
                    j += 1
                else:
                    index = j
                    break
        return strs[0][:index]