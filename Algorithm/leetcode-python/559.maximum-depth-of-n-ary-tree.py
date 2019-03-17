# Time: O(n)
# Space: O(h) h is the height of n-ary tree.

# iterative solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        stack = []
        stack.append((1, root))
        depth = 0
        while stack:
            current_depth, node = stack.pop()
            if node.children == []:
                depth = max(depth, current_depth)
                continue
            for child in node.children:
                stack.append((current_depth + 1, child))
        return depth

# recursive solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1