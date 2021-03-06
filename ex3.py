"""
Demonstration of vertical vs horizontal approach for tables in data storage
"""
from __future__ import division
import random
import string
import timing

# Let's generate big vertical and horizontal structure, and calculate the time difference

# Some helper functions, the implementation is not really important
def get_col_names(num_columns):
    def get_rnd_string(size):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
    size = 10
    return [get_rnd_string(size) for _ in range(num_columns)]

def get_horiz_structure(col_names, num_rows):
    """Creates list with dictinaries"""
    struct = [{name: random.randint(0, max_cell_value) for name in col_names} for _ in range(num_rows)]
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
    res = {name: [random.randint(0, max_cell_value)
                  for _ in range(num_rows)] for name in col_names}
    return res

def delimit_output(num=25):
    """Print delimiter into stdout"""
    print('-'*num)

# Let's generate example tables with 3 columns and 10 rows
max_cell_value = 1000
num_cols = 3
num_rows = 10 
my_columns = get_col_names(num_cols)
my_horiz_struct = get_horiz_structure(my_columns, num_rows)
my_vert_struct = get_vert_structure(my_columns, num_rows)




# Let's print a part of the tables 
print("1. First 5 rows of horizontal structure:")
print_first(my_horiz_struct)
print("\n2. Frits 5 cols of vertical structure:")
print_first(my_vert_struct)




# Implementation of select sum(col) form TABLE
@timing.time_function(unit='seconds', what='sum', digits=7)
def get_sum(struct, col):
    if isinstance(struct, dict): # if struct is vertical
        return sum(struct[col])  # use vertical summ
    else:                        # else use standart loop
        total = 0      
        for line in struct:
            total += line[col]
        return total
            

@timing.time_function(unit='seconds', what='sum filtered', digits=7)
def get_sum_with_filter(table, sum_col_name, filter_col_name, amount):
    """Returns summation of sum_col, where filter_col > amount"""
    result_sum = 0
    if isinstance(table, dict):             # if struct is vertical
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

col_index = 0
horiz_first_col_sum = get_sum(my_horiz_struct, my_columns[col_index])
vert_firts_col_sum = get_sum(my_vert_struct, my_columns[col_index])





print("\n3. Sum of the {} column in horizontal = {} and in vertical = {}".format(
    col_index + 1, horiz_first_col_sum, vert_firts_col_sum))

filter_number = 500
horiz_first_col_sum_filtered = get_sum_with_filter(      
    my_horiz_struct, my_columns[col_index], my_columns[col_index + 1], filter_number)
vert_first_col_sum_filtered = get_sum_with_filter(
    my_vert_struct, my_columns[col_index], my_columns[col_index + 1], filter_number)





print("\n4. Sum of the {} column where {} column > {}: in horizontal = {} and in vertical = {}".format(
    col_index + 1, col_index + 2, filter_number, horiz_first_col_sum_filtered, vert_first_col_sum_filtered))
delimit_output()





# Let's calculate sum and sum with filter on bigger table, and time them
num_cols = 25
num_rows = 100000
my_columns = get_col_names(num_cols)
my_vert_struct = get_vert_structure(my_columns, num_rows)
print('Vertical structure builded')
my_horiz_struct = get_horiz_structure(my_columns, num_rows)
print('Horizontal structure builded\n')
delimit_output()




print("5. Timing for sums without filter")
print("Horizontal")
horiz_first_col_sum = get_sum(my_horiz_struct, my_columns[col_index])
print("Vertical")
vert_first_col_sum = get_sum(my_vert_struct, my_columns[col_index])
delimit_output()





filter_number = 999
print("6. Timing for sums with filter")
print("Horizontal")
horiz_first_col_sum_filtered = get_sum_with_filter(
    my_horiz_struct, my_columns[col_index], my_columns[col_index+1], filter_number)
print("Vertical")
vert_first_col_sum_filtered = get_sum_with_filter(
    my_vert_struct, my_columns[col_index], my_columns[col_index + 1], filter_number)
