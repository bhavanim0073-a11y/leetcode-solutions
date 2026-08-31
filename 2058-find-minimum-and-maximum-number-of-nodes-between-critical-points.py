# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        # Need at least 3 nodes for a critical point
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next

        position = 1

        first = -1
        last = -1

        min_distance = float('inf')
        max_distance = -1

        while curr.next:

            next_node = curr.next

            # Check if curr is a critical point
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val

            if is_max or is_min:

                # First critical point
                if first == -1:
                    first = position
                    last = position

                else:
                    # Distance from previous critical point
                    distance = position - last

                    # Update minimum distance
                    min_distance = min(min_distance, distance)

                    # Update last critical point
                    last = position

                    # Maximum distance is between
                    # first and last critical points
                    max_distance = last - first

            prev = curr
            curr = curr.next
            position += 1

        # Fewer than two critical points
        if min_distance == float('inf'):
            return [-1, -1]

        return [min_distance, max_distance]
