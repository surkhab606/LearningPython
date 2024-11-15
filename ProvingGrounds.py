new_list = ["Johnson", "Canyon", "Mountain", "Leaf-Springs"]


def append_4_to_list(lst):
    lst.append(4)


def our_print(s):
    print(s)


append_4_to_list(new_list)
print(new_list)

b = new_list

print(our_print("Johnson"))

print(b is new_list)

from copy import deepcopy

b = deepcopy(new_list)

print(b)
