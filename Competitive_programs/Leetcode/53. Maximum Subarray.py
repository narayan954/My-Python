class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
    
"""
Using Divide and Conquer
class Solution:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)
"""
