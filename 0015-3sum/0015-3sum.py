class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = []
        nums.sort()
        
        # Track the first element's index dynamically
        k = 0
        i = 1 
        j = len(nums) - 1 
        
        # A single while loop, just like your original structure
        while k < len(nums) - 2:
            if i >= j:
                # When pointers cross, shift the first element index 'k' forward
                k = k + 1
                
                # Skip duplicate values for the first element to avoid duplicate triplets
                while k < len(nums) - 2 and nums[k] == nums[k - 1]:
                    k = k + 1
                    
                # Reset the pointers relative to the new 'k'
                i = k + 1
                j = len(nums) - 1
                continue
            
            # Your exact algebraic match logic, substituting nums[0] with nums[k]
            if ((-(nums[i] + nums[j])) == nums[k]):
                arr.append([nums[k], nums[i], nums[j]])
                i = i + 1
                j = j - 1
                
                # Skip duplicate values for the second and third elements
                while i < j and nums[i] == nums[i - 1]:
                    i = i + 1
                while i < j and nums[j] == nums[j + 1]:
                    j = j - 1
                    
            elif ((-(nums[i] + nums[j])) > nums[k]):
                i = i + 1
            else:
                j = j - 1
                
        return arr