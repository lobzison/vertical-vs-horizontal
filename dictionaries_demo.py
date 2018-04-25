"""
Dictionaries - onordered set of key:value pairs. Keys must be uniuque in a scope of a dictionary, and must be immutable
Implemented as a hash table
acces by key is O(1)
"""

str_to_str = {"key": "value"}
print("\n1. String key to string value")
print(str_to_str)




combined = {"key1": "value1",
            1: 2,
            "1": 3,
            3: 1}

print("\n2. Combined disctionary")
print(combined)
print("\n")



# Accesing the values uses the same syntax as dictionaries

my_value = str_to_str["key"]
print(my_value)

secret_value = combined["1"]
print("\n3. The secret value is:")
print(secret_value)
