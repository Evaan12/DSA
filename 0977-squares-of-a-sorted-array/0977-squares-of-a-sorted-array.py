class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(0,(len(nums))):
            element=nums[i]*nums[i]
            arr.append(element)

        nums[:]=arr
        
        nums.sort()
        return nums

        