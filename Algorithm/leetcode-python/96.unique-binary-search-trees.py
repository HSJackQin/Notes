'''
结题思路：假设n个节点存在二叉排序树的个数是G(n)，
1为根节点，2为根节点，...，n为根节点，当1为根节点时，
其左子树节点个数为0，右子树节点个数为n-1，同理当2为根节点时，
其左子树节点个数为1，右子树节点为n-2，所以可得
G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
'''

# 动态规划
# Time: O(n^2)
# Space: O(n)
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = [1,1]
        if n == 0:
            return 1
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += counts[j]*counts[i-j-1]
            counts.append(count)
        return counts[-1]