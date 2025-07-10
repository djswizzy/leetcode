class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            result = pairs.get(nums[i],None)
            if (result != None) and (result != i):
                return [i,result]
            pairs[target - nums[i]] = i

        
