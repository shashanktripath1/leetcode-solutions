# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kp,fp,sp=head,head,head
        for i in range(k-1):
            kp=kp.next
        fp=kp
        while (fp.next):
            fp=fp.next
            sp=sp.next
        kp.val,sp.val=sp.val,kp.val
        return head
            