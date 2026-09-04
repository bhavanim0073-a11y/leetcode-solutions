class Solution(object):

    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next and current.next.next:

            first = current.next
            second = current.next.next

            # Swap the two nodes
            first.next = second.next
            second.next = first
            current.next = second

            # Move to the next pair
            current = first

        return dummy.next
