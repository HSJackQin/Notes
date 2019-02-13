class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList: return 0
        if beginWord in wordList: wordList.remove(beginWord)
        res,forward,backward= 2,{beginWord},{endWord}
        letters,length = set('qwertyuioplkjhgfdsazxcvbnm'),len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward,backward = backward,forward#交换后每次都从小集合中遍历
            cur = set()#相当于层次序遍历中的新一层
            for word in forward:
                for idx in range(length):
                    x,y = word[:idx],word[idx+1:]
                    for letter in letters:
                        temp = x + letter + y
                        if temp in backward: return res
                        if temp in wordList:
                            cur.add(temp)#这里将与forward中单词只差一个字母的有效单词加入，因为该题只要求最短距离，所以已达到的都删除，避免重复访问。连visited数组都省下了
                            wordList.remove(temp)
            res += 1
            forward = cur
        return 0