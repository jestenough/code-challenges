def runningSum(nums) -> list:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums