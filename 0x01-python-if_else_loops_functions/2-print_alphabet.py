#!/usr/bin/python3
print("".join(chr(i) for i in range(ord('a'), ord('z') + 1)), end="")

# VERSION1
# for i in range(97, 123):
#    print(chr(i), end="")

# VERSION2
# for i in range(97, 123):
#    print("{:c}".format(i), end="")

# VERSION3
# import string
# print(string.lower_case[::], end="")
