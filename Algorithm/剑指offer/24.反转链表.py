### 24.反转链表

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pPre = None
        pNode = pHead
        pReverseHead = None
        while pNode is not None:
            pNext = pNode.next
            if pNext is None:
                pReverseHead = pNode
            pNode.next = pPre
            pPre = pNode
            pNode = pNext
        return pReverseHead