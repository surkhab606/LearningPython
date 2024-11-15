new_list = ["Johnson", "Canyon", "Mountain", "Leaf-Springs"]


def append_4_to_list(lst):
    lst.append(4)


append_4_to_list(new_list)
print(new_list)

b = new_list

print(b is new_list)