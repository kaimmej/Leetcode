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

    # how do i delete from an array?
    # del simpleArray[0]


    # 
    #
    #   ITERATING
    for i, num in enumerate(nums):
        print(f"Index: {i}, Value: {num}")




    #
    #
    #   LIST OF STRINGS

    # How can i add a string to the list?
    list_a = ["watermelon", "peach", "cherry"]
    list_b = ["apple", "orange", "banana"]

    # Concatenating two lists
    combinedList = list_a + list_b
    print(combinedList)

    # List of lists
    list_of_lists = [list_a, list_b]
    print(list_of_lists)

main()