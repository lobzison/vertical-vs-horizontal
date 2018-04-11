"""
Demonstration of vertical vs horizontal approach for tables in data storage
"""
from __future__ import division
import random
import string
import timing

# Let's generate big vertical and horizontal structure, and calculate the time difference
max_value = 1000
def get_col_names(num_columns):
    def get_rnd_string(size):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
    size = 10
    return [get_rnd_string(size) for _ in range(num_columns)]

def get_horiz_structure(col_names, num_rows):
    """Creates list with dictinaries"""
    struct = [{name: random.randint(0, max_value) for name in col_names} for _ in range(num_rows)]
    return struct

def print_first(my_struct, num=5):
    i = 0
    for line in my_struct:
        if isinstance(line, dict): 
            print(line)
        else:
            print("{}: {}".format(line, my_struct[line]))
        if i > num:
            break
        i += 1

def get_vert_structure(col_names, num_rows):
    res = {name: [random.randint(0, max_value) for _ in range(num_rows)] for name in col_names}
    return res


num_cols = 3
num_rows = 10 
my_columns = get_col_names(num_cols)
my_horiz_struct = get_horiz_structure(my_columns, num_rows)
my_vert_struct = get_vert_structure(my_columns, num_rows)

print_first(my_vert_struct)

# implementation of select sum(col) form TABLE
@timing.time_function(unit='seconds')
def get_sum(struct, col):
    if isinstance(struct, dict):
        return sum(struct[col])
    else:
        total = 0
        for line in struct:
            total += line[col]
        return total
            
@timing.time_function(unit='seconds')
def get_sum_with_filter(table, sum_col_name, filter_col_name, amount):
    """Returns summation of sum_col, where filter_col > amount"""
    result_sum = 0
    if isinstance(table, dict):
        filter_col = table[filter_col_name] # load whole filter column
        sum_col = table[sum_col_name]       # load whole sum column
        for idx in range(len(filter_col)):  # starting from 0 to the lenght of filter column
            if filter_col[idx] > amount:    # if value of filter column on that index is > that amount
                result_sum += sum_col[idx]  # add value of sum column on that index to total summ
    else:
        for line in table:
            if line[filter_col_name] > amount:
                result_sum += line[sum_col_name]
    return result_sum

print_first(my_horiz_struct, 10)

print (get_sum(my_horiz_struct, my_columns[0]),
       get_sum(my_vert_struct, my_columns[0]))

print (get_sum_with_filter(my_horiz_struct, my_columns[0], my_columns[1], 500),
       get_sum_with_filter(my_vert_struct, my_columns[0], my_columns[1], 500))


num_cols = 25
num_rows = 100000
my_columns = get_col_names(num_cols)
my_vert_struct = get_vert_structure(my_columns, num_rows)
print('end of vert')
my_horiz_struct = get_horiz_structure(my_columns, num_rows)
print('end of goriz')


print (get_sum(my_horiz_struct, my_columns[0]),
       get_sum(my_vert_struct, my_columns[0]))

print (get_sum_with_filter(my_horiz_struct, my_columns[0], my_columns[1], 500),
       get_sum_with_filter(my_vert_struct, my_columns[0], my_columns[1], 500))

# TODO: output formatting