"""
Demonstration of vertical vs horizontal approach for tables in data storage

Part one - general idea

Classical DB table structure(horizontal):
columns gouped into a row, even if we want to get value from one colums
we still acess the whole row
"""

# Lets use a example table:
# CREATE TABLE horizontal(trade_id number, quantity number)

# INSERT INTO horizontal values(
#     1, 15
# );
# INSERT INTO horizontal values(
#     1, 28
# );
# INSERT INTO horizontal values(
#     1, 19
# );
# INSERT INTO horizontal values(
#     1, 32
# );

# select * from horizontal

# trade_id|quantity
#     1       15
#     2       28
#     3       19
#     4       32

# As a high level abstraction table  can be represented as following python structure

horizontal = [{"trade_id": 1, "quantity": 15},
              {"trade_id": 2, "quantity": 28},
              {"trade_id": 3, "quantity": 19},
              {"trade_id": 4, "quantity": 32}]

# If we want to retrieve values from the structure - we can use syntax - horizontal[rowid][col_name]
print("\n1. Quantity of the first trade:")
print(horizontal[0]["quantity"])





# Get sum of all quantities of all trades 
my_sum = 0
for trade in horizontal:        # for all rows in table
    my_sum += trade["quantity"] # add up the quantities

print("\n2. Summ of all trades is:")
print(my_sum)






#-------------------------------------------------
# Lets try to verticly represent the same DB table
# trade_id|quantity
#     1       15
#     2       28
#     3       19
#     4       32

vertical = {"trade_id": [1, 2, 3, 4],
            "quantity": [15, 28, 19, 32]}

print("\n3. Quantity of the first trade vertical:")
v_firts = vertical["quantity"][0]
print(v_firts)






print("\n4. Summ of all trades vertical is:")

# Brute froce approach
v_sum = 0
for quanity in vertical["quantity"]:
    v_sum += quanity

print (v_sum)

# But vectorization can be used
# TODO: vectrorization of summation or why is it faster
# https://stackoverflow.com/questions/35091979/why-is-vectorization-faster-in-general-than-loops
# 

v_sum = sum(vertical["quantity"])
print (v_sum)


# Geat example http://qr.ae/TU1SUO
# https://www.slideshare.net/arangodb/introduction-to-column-oriented-databases
