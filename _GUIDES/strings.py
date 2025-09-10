

def main():


    # 
    #
    # SubStrings
    #   string[start:end:step]
    string = "freeCodeCamp"

    print(string[0:5])  # get the first 5 characters
    print(string[-5:])  # get the last 5 characters
    print(string[::2])  # get every other character

    # how can i ignore the first character of a string?
    print(string[1:])

    #
    #
    # Append a string to another string
    string += " is awesome!"
    print(string)



    # Iterating, filtering, mapping... 
    def isPalindrom(self, s: str) -> bool:

        # FILTER
        # filter returns an iterable filter object. 
        #   - the function is applied to each element. if function(element) == True, the element is kept.
        #   - result is a lazy iterator (not a string/list)
        filtered_chars = filter(lambda ch: ch.isalnum(), s)


        # MAP
        # map applies the function to each element and returns a map object (another lazy iterator...)
        # So map is being applied to each object that was returned by the first filtering function. 
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list


main()