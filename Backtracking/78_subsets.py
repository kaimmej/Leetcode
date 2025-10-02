class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # How do i do backtracking? This is recursion right? 

        lenNums = len(nums)
        res = []
        res.append([])
        

        for i in range(lenNums):
            curr_num = nums[i]
            print(curr_num)
            resLength = len(res)

            for j in range(resLength):
                print(f" BEFORE: {res[j]}")
                # Add num i
                # I dont think this works, I think these are references to the same variable.
                tmp_list = res[j]
                new_list = tmp_list.copy()

                new_list.append(curr_num)
                res.append(new_list)

                print(f" AFTER: {res[j]}")
                print(f" res: {res}")


            # For every number, we do 2 things, recursively...
            #   - we DO NOT add this number to every subset
            #   - we DO add this ...
        
        return res
        