"""
Demonstration of vertical vs horizontal approach for tables in data storage

Final part
"""

# Also to consider - its much easier to compress data, epecialy varchar

# Final conclusion
# Row storage are great for reteiwing one or few rows
# Row storage are great at updating\deletion

# Columnar storage are great for full table\partition query on few columns
# Columnar storafe still shows performance increace even with filtering

# Rule of a thumb - if your queries maily accesess few rows and lots of columns - row storage is great
#                   if your queries maily accesess few columns and a lot of rows - columnar storage can offer much better performance


# Additional links:
# Geat example http://qr.ae/TU1SUO
# Presentation of different storage types: https://www.slideshare.net/arangodb/introduction-to-column-oriented-databases
