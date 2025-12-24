from typing import List
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = set(nums)
        ans = []
        for i in range(0,len(nums)):
            if i+1 not in numset:
                ans.append(i+1)
        return ans
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))