

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
# Example 1:
#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        keyDict = {}

        for s in strs:
            key = tuple(sorted(s))

            if key in keyDict:
                keyDict[key].append(s)
            else:
                keyDict[key] = [s]
        
        for listS in keyDict.values():
            output.append(listS)
        return output
        

# NOTES:
    #
    #   key = tuple(sorted(s))
    #   sorted(s) returns a list of the characters of the string in sorted order.
    #   tuple() converts the list into a tuple. which is basically a list or a string
    #


# Oct 5th 2024
# I like this solution too. 
# I like the naming that i did here more than before... 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_anagrams_dictionary = {}
        for str in strs:
            # print(f"{str=}")
            sorted_str = ''.join(sorted(str))
            #print(f"{sorted_str=}")
            if sorted_str not in grouped_anagrams_dictionary:
                # we must create a new list that just contains the new element. 
                grouped_anagrams_dictionary[sorted_str] = []

            grouped_anagrams_dictionary[sorted_str].append(str)
        print(grouped_anagrams_dictionary)

        result = []
        for anagram_group in grouped_anagrams_dictionary.values():
            result.append(anagram_group)
        return result