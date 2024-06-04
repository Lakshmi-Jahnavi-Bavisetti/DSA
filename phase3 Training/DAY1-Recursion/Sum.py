def add(i,list1,sum1):
    if(i<len(list1)):
        sum1+=list1[i]
        add(i+1,list1,sum1)
    else:
        print(sum1)
        return
list1=[1,2,3,4,5]
i=0
sum1=0
add(i,list1,sum1)

# Passing data from Parent function to child function
def printSum(index, n, nums, result):
    if index == n:
        print("Sum is:", result)
        return 
 
    result += nums[index]
    #result = result + nums[index]
    printSum(index + 1, n, nums, result)
 
# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)

