class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 0.5
        nums[:] = [x for x in nums if x != 0.5]
        
        k = len(nums)
        return k
