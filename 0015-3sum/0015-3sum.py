class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # i=0  <-- Removed: The 'for' loop does this automatically
        arr=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            # FIX: Moved j and k inside the loop so they reset for every 'i'
            j=i+1
            k=len(nums)-1
            
            while j<k:
                if (nums[i]+nums[k]+nums[j]<0):
                    j=j+1
                elif (nums[i]+nums[k]+nums[j]>0):
                    k=k-1
                else:
                    arr.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    
                    # Your duplicate skip for j works great!
                    while j<k and nums[j]==nums[j-1]:
                        j=j+1
    
        return arr