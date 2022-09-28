def removeElement(nums, val) -> int:
    n = len(nums)
    left = 0
    dic={}
    for right in range(0, n):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left

print(removeElement([3,2,2,3],3))