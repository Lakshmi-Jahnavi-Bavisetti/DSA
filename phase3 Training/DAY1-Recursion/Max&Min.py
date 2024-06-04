def printMax(index, n, nums, result):
    if index == n:
        print("Max ele is:", result)
        return 
 
    result=max(result,nums[index])
    printMax(index + 1, n, nums, result)
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printMax(1, n, nums,nums[0])

# Passing data from child function to Parent function
def printMax2(index, n, nums):
    if index == n:
        return 0 
    max1 = printMax2(index + 1, n, nums)
    return max(max1,nums[index])
nums = [12, 34,39, 12, 5, 7]
n = len(nums)
result = printMax2(0, n, nums)
print("Max is:", result)

def printMin(index, n, nums, result):
    if index == n:
        print("Max ele is:", result)
        return 
 
    result=min(result,nums[index])
    printMin(index + 1, n, nums, result)
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printMin(1, n, nums,nums[0])

def printMin2(index, n, nums):
    if index == n:
        return nums[0]
    min1 = printMin2(index + 1, n, nums)
    return min(min1,nums[index])
nums = [12, 34,39, 12, 5, 7]
n = len(nums)
result = printMin2(0, n, nums)
print("Min is:", result)




##################################################
def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] > result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater < nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)