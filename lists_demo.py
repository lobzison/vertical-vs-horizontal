"""Small intro into python data types
lists - compound data type, ordered, can contain different data types
access by index is O(1)
Examples of list:
"""
empty_list = []
print("Empty list:")
print(empty_list)

int_list = [1, 2]
print('\nInteger list:')
print(int_list)

str_list = ["one", "two", "three"]
print('\nString list:')
print(str_list)

comb_list = [1, "two", 3.0, [1]]
print('\nCombined list, with nested list:')
print(comb_list)

# Accesing the elements in the list:
fist_elem = str_list[0]
print('\nFirst element of a string list:')
print(fist_elem)
