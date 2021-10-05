class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        largest_sum = dp[0]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[i] > largest_sum:
                largest_sum = dp[i]
        
        return largest_sum