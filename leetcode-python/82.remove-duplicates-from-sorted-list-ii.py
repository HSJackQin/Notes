'''
本题和上一题(83.remove-duplicates-from-sorted-list)相比，有两个地方要注意：
（1）设置空的头节点指向第一个节点(head)，并保持指针的后继节点指向下一个unique的节点
（2）另设一个扫描的指针用来判断元素是否是unique的
'''

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        temp, pre = dummy, head
        while temp.next and temp.next.next:
            k = 0
            while pre.next and pre.next.val == pre.val:
                k = 1
                pre = pre.next
            if k == 0:
                temp = temp.next
            else:
                temp.next = pre.next
            pre = pre.next
        return dummy.next