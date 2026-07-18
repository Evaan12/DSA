class Solution:
    def sortColors(self, nums: List[int]) -> None:
        one=0
        zero=0
        two=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero=zero+1
            elif nums[i]==1:
                one=one+1
            else:
                two=two+1
        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i < zero + one:
                nums[i] = 1
            else:
                nums[i] = 2
