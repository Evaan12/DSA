class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        
        # 1. Split into negatives and positives
        for num in nums:
            if num < 0:
                negatives.append(num * num)  # Square it right away
            else:
                positives.append(num * num)  # Square it right away
        
        # 2. Since negatives were sorted from most-negative to least-negative (e.g., -4, -1),
        # squaring them makes them decreasing (16, 1). We must reverse them to make them sorted (1, 16).
        negatives = negatives[::-1]
        
        # 3. Merge the two sorted arrays (positives and negatives) back into nums
        i = 0  # Pointer for negatives
        j = 0  # Pointer for positives
        index = 0  # Pointer for rewriting nums
        
        # Compare and merge
        while i < len(negatives) and j < len(positives):
            if negatives[i] < positives[j]:
                nums[index] = negatives[i]
                i += 1
            else:
                nums[index] = positives[j]
                j += 1
            index += 1
            
        # 4. Clean up any remaining elements
        while i < len(negatives):
            nums[index] = negatives[i]
            i += 1
            index += 1
            
        while j < len(positives):
            nums[index] = positives[j]
            j += 1
            index += 1
            
        return nums