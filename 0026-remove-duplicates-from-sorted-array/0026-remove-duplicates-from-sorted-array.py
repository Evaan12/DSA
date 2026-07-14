class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=[nums[0]]
     
        for i in range(1,(len(nums))):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])
            
        nums[:]=arr
