# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Using MergeSort to solve in O(NlogK)

        if not lists or len(lists)==0:
            return None

        while len(lists) > 1:
            print(len(lists))
            res = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None

                res.append(self.mergeList(l1,l2))

            lists = res
        
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        head = dummy
        
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return dummy.next

