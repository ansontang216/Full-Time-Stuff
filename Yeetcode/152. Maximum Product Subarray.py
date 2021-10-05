class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = [0] * len(nums)
        min_product = [0] * len(nums)
        
        max_product[0] = nums[0]
        min_product[0] = nums[0]
        
        for i in range(1, len(nums)):
            max_product[i] = max(nums[i], max_product[i-1] * nums[i], min_product[i-1] * nums[i])
            min_product[i] = min(nums[i], min_product[i-1] * nums[i], max_product[i-1] * nums[i])
        return max(max_product)