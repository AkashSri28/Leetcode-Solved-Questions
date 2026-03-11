from sortedcontainers import SortedList
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        sl = SortedList()

        l = 0
        for r in range(len(nums)):
            if r - l > indexDiff:
                sl.remove(nums[l])
                l += 1

            pos = sl.bisect_left(nums[r]-valueDiff)
            if pos < len(sl) and sl[pos] <= nums[r]+valueDiff:
                print(nums[r], pos, len(sl))
                return True

            sl.add(nums[r])

        return False

        # TC: O(nlogk)
        # SC: O(k)
        # Approach: use sortedlist to store elements in a sorted list. Now find the element where nums[r]-val can be inserted. Check if there is an element already here. If yes, then check if element <= nums[r]+val

        