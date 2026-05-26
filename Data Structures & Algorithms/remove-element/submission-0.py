class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l , r = 0 , len(nums)-1
        count = 0
        while(l<=r):
            if nums[l]==val:
                count+=1
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            else:
                l+=1
        return len(nums)-count
        