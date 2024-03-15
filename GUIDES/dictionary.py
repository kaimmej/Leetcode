# METHODS
#
#   values() - returns a list of all the values in the dictionary
#   keys() - returns a list of all the keys in the dictionary
#   pop() - removes the element with the specified key
#
#

def methods():
    print("METHODS:")
    print("===================================")
    # values():
    #  returns a list of all the values in the dictionary. Its an iterable that can be used in a for loop 
    users: dict = { 0: 'Mario', 1: 'Luigi', 2: 'Peach' }
    print(users.values()) # ['Mario', 'Luigi', 'Peach']

    # keys():
    #  returns a list of all the keys in the dictionary. Its an iterable that can be used in a for loop
    print(users.keys()) # [0, 1, 2]

    # pop():
    #  removes the element with the specified key
    users.pop(0)
    print(users) # {1: 'Luigi', 2: 'Peach'}
    #  Something thats nice about pop is that it returns the value of the key that was removed
    #  If you try to pop something that doesn't exist - you get a key error
    popped = users.pop(1)
    print(popped) # Luigi

    # popitem():
    #  removes the last inserted key-value pair
    users.popitem()
    print(users) # {}


def main():
    
    letterCountDictionary = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
    print(letterCountDictionary)
    print()
    print()

    # Accessing elements 
    print("ACCESS:")
    print("===================================")
    print("   singleItem: ", letterCountDictionary['a'])
    print("   keys: ",letterCountDictionary.keys())
    print("   values: ",letterCountDictionary.values())
    print("   Items: " , letterCountDictionary.items())
    print("   get: ", letterCountDictionary.get('a'))
    print("   (if no) get: ",           letterCountDictionary.get('z'))
    print("   (if no) get: ",           letterCountDictionary.get('z', 0))
    print("   (if no) get: ",           letterCountDictionary.get('z', 'Not Found'))
    print("   (if no) setdefault: ",    letterCountDictionary.setdefault('z', 0))
    print("  ", letterCountDictionary)
    print()


    for key in letterCountDictionary:
        print(key, letterCountDictionary[key])
    

    # Adding elements 
    letterCountDictionary['f'] = 6
    letterCountDictionary.update({'h': 8})

    # Removing elements
    letterCountDictionary.pop('a')
    del letterCountDictionary['b']
    letterCountDictionary.popitem()
    # letterCountDictionary.clear()
    print(letterCountDictionary)

    # Contains key
    print('a' in letterCountDictionary)
    print('b' in letterCountDictionary)
    if 'c' in letterCountDictionary:
        print('c is present')

    # contains value 
    print(1 in letterCountDictionary.values())
    if 3 in letterCountDictionary.values():
        print('3 is present')


methods()
main()