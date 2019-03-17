### 25.合并两个排序的链表

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        MergeList = ListNode(0)
        if pHead1.val < pHead2.val:
            MergeList.next = pHead1
            MergeList.next.next = self.Merge(pHead1.next, pHead2)
        else:
            MergeList.next = pHead2
            MergeList.next.next = self.Merge(pHead1, pHead2.next)
        return MergeList.next# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        MergeList = ListNode(0)
        if pHead1.val < pHead2.val:
            MergeList.next = pHead1
            MergeList.next.next = self.Merge(pHead1.next, pHead2)
        else:
            MergeList.next = pHead2
            MergeList.next.next = self.Merge(pHead1, pHead2.next)
        return MergeList.next