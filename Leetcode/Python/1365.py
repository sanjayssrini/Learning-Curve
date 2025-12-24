from typing import List
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums=sorted(nums)
        ans=[]
        for i in range(0, len(nums)):
            ans.append(new_nums.index(nums[i]))
        return ans

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
