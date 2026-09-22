class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        dummy = ListNode()
        current = dummy

        while curr1 is not None and curr2 is not None:

            if curr1.val <= curr2.val:
                current.next = curr1
                curr1 = curr1.next
            else:
                current.next = curr2
                curr2 = curr2.next

            current = current.next

        # Attach whichever list still has nodes
        if curr1 is not None:
            current.next = curr1
        else:
            current.next = curr2

        return dummy.next