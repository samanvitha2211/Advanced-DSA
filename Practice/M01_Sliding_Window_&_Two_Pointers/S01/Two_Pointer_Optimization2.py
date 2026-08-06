"Remove Duplicates from Sorted Array"

'''from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))'''

"Remove Element"

'''from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
nums = [3,2,2,3] 
val = 3
print(removeElement(nums, val))'''

"Two Sum II - Input array is sorted"

from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    l,r=0, n-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1,r+1]
        elif s > target:
            r -= 1
        else:
            l += 1
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))