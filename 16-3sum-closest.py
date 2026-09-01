class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        n = len(nums)

        # Start with the first possible sum
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                # Exact target found
                if current == target:
                    return current

                # Update closest sum
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Move pointers
                if current < target:
                    left += 1
                else:
                    right -= 1

        return closest
