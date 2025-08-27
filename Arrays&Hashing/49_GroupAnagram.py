

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
# Example 1:
#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs):
        
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
    def groupAnagrams(self, strs):
        
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
    




#
#
# Solution 3 
    def groupAnagrams(self, strs):
        
        result = {} # mappings of the frequencyArrays to the list of words that were given

        for word in strs:
            frequencyArray = self.parseWord_intoFrequencyArray(word)
            # print(f" {word} : {frequencyArray}")

            if frequencyArray not in result:
                # print("NEW")
                result[frequencyArray] = []
            
            result[frequencyArray].append(word)
        
        returnList = []

        for wordList in result.values():
            returnList.append(wordList)
        

        return returnList




    def parseWord_intoFrequencyArray(self, s: str):
        
        # Character count array, initialized to zeros and we want it to be 26 long. 
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1
        
        return tuple(count)