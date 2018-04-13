from __future__ import division
"""
Demonstration of vertical vs horizontal approach for tables in data storage
"""
# # Example two
# CREATE TABLE BIG_TABLE(trade_id number(10 byte) NOT NULL,
#                             quantity number(10 byte) NOT NULL,
#                             ISIN     char(30 byte),
#                             clinet   char(30 byte),
#                             domain   char(10 byte),
#                             code1    char(30 byte),
#                             code2    char(30 byte),
#                             code3    char(30 byte))

def calc_gb_size(num_rows, row_size):
    """Calculate the size of table in GB 
    given row size and number of rows in bytes"""
    total_byte = row_size * num_rows
    total_gb = ((total_byte / 1024) / 1024) / 1024
    return total_gb

# we want to get results for followin query: 
# select sum(quantity) from BIG_TABLE

# Lets calculate I/O needed to calculate sum(quantity) with horizontal
size_of_row = 10 + 10 + 30 + 30 + 10 + 30 + 30 + 30
num_of_rows = 100000000 # 100mil
print('\nI/O needed to calculate sum(quantity) with horizontal:')
print(calc_gb_size(size_of_row, num_of_rows))


#Now the same for vertical
size_of_row = 10
num_of_rows = 100000000 # 100mil
print('\nI/O needed to calculate sum(quantity) with vertical:')
print(calc_gb_size(size_of_row, num_of_rows))

# In real world we use much more complicated queries than just aggregate function over the whole table
# les'l look at the simple filtration
# select sum(quantity) from BIG_TABLE where code2 > 10 000
# for horizontal approach I/O will remain the same
# lest look how we can get it with vertical

vertical = {"trade_id": [1, 2, 3, 4],
            "quantity": [15, 28, 19, 32],
            "ISIN":     ["KLNJU", "LLLQK", "KNKNK", "PQRFG"],
            "clinet":   ["ASDFD", "FSAFF", "GADSF", "ASDFF"],
            "domain":   ["REGEH", "ASFWF", "AWFEF", "QWEFQ"],
            "code1":    ["ERHRH", "ASFWF", "ASFWF", "ASFFW"],
            "code2":    ["ERHRH", "DFFHH", "DFHFH", "FDGHH"],
            "code3":    [1884, 1233, 122, 7434]}

def get_sum_with_filter(table, sum_col_name, filter_col_name, amount):
    """Returns summation of sum_col, where filter_col > amount"""
    filter_col = table[filter_col_name] # load whole filter column
    sum_col = table[sum_col_name]       # load whole sum column
    result_sum = 0
    for idx in range(len(filter_col)):  # starting from 0 to the lenght of filter column
        if filter_col[idx] > amount:    # if value of filter column on that index is > that amount
            result_sum += sum_col[idx]  # add value of sum column on that index to total summ

    print('\nThe summ of {} column with {} column > {} is {}' # print formatted results
          .format(sum_col_name, filter_col_name, amount, result_sum))

get_sum_with_filter(vertical, "quantity", "code3", 2000)

print('\nmax I/O needed to calculate sum(quantity) with vertical and one condition:')
size_of_row = 10 + 30
num_of_rows = 100000000 # 100mil
print(calc_gb_size(size_of_row, num_of_rows))

