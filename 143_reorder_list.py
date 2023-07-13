# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Step 1 - Split the list into two portions
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #Step 2 - Reverse the second portion
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        #here prev is the head for the second portion

        #Step 3 - Merging the two portions
        first, sec = head, prev
        while sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1
            first, sec = tmp1, tmp2
