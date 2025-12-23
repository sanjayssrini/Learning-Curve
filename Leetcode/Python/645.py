from typing import List
def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numset = set()
        repeat = -1
        for num in nums:
            if num in numset:
                repeat = num
            numset.add(num)
        for i in range(1, n+1):
            if i not in numset:
                missing = i
                break
        return [repeat, missing]
print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1])) 