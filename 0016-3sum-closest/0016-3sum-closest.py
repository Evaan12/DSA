class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=0
        maxdiff=float('inf')
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<target:
                    diff=abs(target-sum)
                    j=j+1
                    if (diff<maxdiff):
                        maxdiff=diff
                        close=sum
                elif (sum>target):
                    diff=abs(target-sum)
                    k=k-1
                    if (diff<maxdiff):
                        maxdiff=diff
                        close=sum
                else:
                    close=sum
                    j=j+1
                    k=k-1
        return close 
           