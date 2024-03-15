
def main():
    
    letterCountDictionary = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
    print(letterCountDictionary)
    print()
    print()

    # Accessing elements 
    print("ACCESS:")
    print("   singleItem: ", letterCountDictionary['a'])
    print("   keys: ",letterCountDictionary.keys())
    print("   values: ",letterCountDictionary.values())
    print("   Items: " , letterCountDictionary.items())
    print("   get: ", letterCountDictionary.get('a'))
    print("   (if no) get: ", letterCountDictionary.get('z'))
    print("   (if no) get: ", letterCountDictionary.get('z', 0))
    print("   (if no) get: ", letterCountDictionary.get('z', 'Not Found'))
    print("   (if no) setdefault: ", letterCountDictionary.setdefault('z', 0))
    print("  ", letterCountDictionary)
    print()


    for key in letterCountDictionary:
        print(key, letterCountDictionary[key])
    

    # Adding elements 
    letterCountDictionary['f'] = 6
    letterCountDictionary.append('g', 7)
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


main()