class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        if len(nums) == 1:
            return nums
        
#         left = [0] * len(nums)
#         right = [0] * len(nums)
        
#         prod = [0] * len(nums)
        
#         left[0] = 1
#         right[len(nums)-1] = 1
        
#         for i in range(1,len(nums)):
#             left[i]  = nums[i-1] * left[i-1]
            
#         for i in range(len(nums)-2, -1, -1):
#             right[i] = nums[i+1] * right[i+1]
        
#         for i in range(len(nums)):
#             prod[i] = left[i] * right[i]
            
#         return prod
        
        prod = [0] * len(nums)
        temp = 1
        
        for i in range(len(nums)):
            prod[i] = temp
            temp = nums[i] * temp
        
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i] = prod[i]*temp
            temp = nums[i] * temp
        
        return prod