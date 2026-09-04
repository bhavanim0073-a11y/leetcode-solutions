class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the current group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Connect previous part to reversed group
            old_first = group_prev.next
            group_prev.next = kth

            # Move to the next group
            group_prev = old_first
