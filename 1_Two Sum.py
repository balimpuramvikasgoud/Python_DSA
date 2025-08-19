class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        num_lit = {}
        for i,  num in  enumerate(nums):
            complement = target-num
            if complement in num_lit:
                return(num_lit[complement],i)
            num_lit[num]=i
        return []


    