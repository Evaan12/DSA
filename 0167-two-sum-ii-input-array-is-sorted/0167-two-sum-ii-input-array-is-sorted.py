class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       sum=0
       i=0
       j=len(numbers)-1
       while i<j:
        sum=numbers[i]+numbers[j]
        if target==sum:
            return [i+1,j+1]
        elif target<sum:
            j=j-1
        else:
            i=i+1