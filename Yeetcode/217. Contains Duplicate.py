class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for number in nums:
            dictionary[number] = dictionary.get(number,0) + 1
            if(dictionary.get(number) > 1):
                return True
        return False