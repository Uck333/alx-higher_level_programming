#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = 0
    k = 0
    try:
        for _ in my_list:
            j = j + 1
        for _ in my_list[:x]:
            k = k + 1
            print(_, end="")
        print("\t")
        if k <= j:
            return k
    except ValueError:
        print("Omg! There are more elements than my_list contains.")


#VERSION 2
#def safe_print_list(my_list=[], x=0):
#    j = 0
#    k = 0
#    try:
#        for i in range (len(my_list[])):
#            j = j + 1
#        for x in range (len(my_list[])):
#            k = k + 1
#            print(my_list[x], end="\n")
#        if k <= j:
#            return k
#    except ValueError:
#        print("Omg! There are more elements than my_list contains.")
