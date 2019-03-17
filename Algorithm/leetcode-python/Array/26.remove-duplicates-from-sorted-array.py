# Time: O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        step = 1
        if len(nums) == 0:
            return None
        while i < len(nums) - 1:
            j = i
            while nums[i] == nums[j] and j < len(nums) - 1:
                j += 1
            if j == len(nums) - 1 and nums[j] == nums[i]:
                return step
            else:
                nums[step] = nums[j]
                i = j
                step += 1
        return step

    def removeDuplicates2(self, A):
        if not A:
            return 0

        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                if not same:
                    last += 1
                    A[last] = A[i]
            i += 1

        return last + 1
