

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


main()