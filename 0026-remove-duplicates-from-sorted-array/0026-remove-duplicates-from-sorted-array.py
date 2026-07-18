class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        officer=0
        cm=1
        res=1
        while cm<len(nums):
            if nums[cm]==nums[cm-1]:
                cm=cm+1
                continue
            nums[officer+1]=nums[cm]
            officer=officer+1
            res=res+1
            cm=cm+1
        return res
