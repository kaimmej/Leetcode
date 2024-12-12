def main():
    nums = [1,2,3,4,5]

    # initialize array to a specific length.
    # This allows you to index into it.
    simpleArray = [1] * len(nums)

    # FORWARDS
    prefix = 1
    for i in range(len(nums)):
        simpleArray[i] = prefix
        prefix *= nums[i]
    
    # BACKWARDS
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        simpleArray[i] *= postfix
        postfix *= nums[i]



main()