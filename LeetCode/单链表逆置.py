"""
单链表的逆置
算法思想：逆置链表初始为空，表中节点从原链表中依次“删除”，
再逐个插入逆置链表的表头（即“头插”到逆置链表中），
使它成为逆置链表的“新”的第一个结点，如此循环，直至原链表为空。

"""

class Solution:
    def __init__(self, data):
        self.data = data
        self.next = None

    def ReversList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

