class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        vote = 1
        for i in range(1, len(nums)):
            if vote == 0 :
                candidate  = nums[i]
                vote = 1
                continue
            if nums[i]==candidate:
                vote+=1
            else:
                vote-=1
        return candidate
            