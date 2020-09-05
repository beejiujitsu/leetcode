# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = []
        while head is not None:
            value = head.val
            b.append(value)
            head = head.next
        joined = "".join((str(c) for c in b))
        return int(f"0b{joined}", base=2)
