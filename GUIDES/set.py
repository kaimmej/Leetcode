
def main():
    
    letterSet = {'a', 'b', 'c', 'd', 'e'}
    b_letterSet = set("abcdefghijklmnopqrstuvwxyz")
    c_letterSet = set("abcdefg")

    print(letterSet)
    print()
    print()

    # Accessing elements 
    print("ACCESS:")
    # print("   singleItem: ", letterS)


    print()


    # set operations
    print("SET OPERATIONS:")
    print("   set_b: ", b_letterSet)
    print("   set_c: ", c_letterSet)
    print("   Union: ", b_letterSet | c_letterSet)
    print("   Intersection: ", b_letterSet & c_letterSet)           # Letters in both b and c
    print("   Difference: ", b_letterSet - c_letterSet)             # Letters in b but not in c
    print("   Symmetric Difference: ", b_letterSet ^ c_letterSet)   # Letters in b or c but not in both
    print("   isSubset: ", c_letterSet.issubset(b_letterSet))       # c is a subset of b
    print("   isSuperset: ", b_letterSet.issuperset(c_letterSet))   # b is a superset of c
    print("   isDisjoint: ", b_letterSet.isdisjoint(c_letterSet))   # b and c have no elements in common
    print()
    

    # list comprehension
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)


    # Removing elements


    # Contains key


    # contains value 



main()