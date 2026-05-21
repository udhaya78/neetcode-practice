# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         s = set()
#         for i in nums:
#             if i in s:
#                 return True
#             s.add(i)
#         return False
class Solution:
    def hasDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False