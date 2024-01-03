#!/usr/bin/python3
for i in range(97, 123):
    if i in [101, 113]:
        continue
    print("{:c}".format(i), end="")

# VERSION2
# for i in range(97, 123)
#    print("{:c}", end="")

# VERSION3
# import string
# print(string.lower_case[::], end="")
