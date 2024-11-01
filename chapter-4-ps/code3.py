# 3. Check that a tuple type cannot be changed in python.

tuple = (1 , 2 , 3)

# tuple.append(3) throw an error because tuple is imutable.
print(tuple)

# if you want to append things in tuple so u can do type conversations by tuple to list. and after changing you can convert list to tuple.

tuple = (1, 2, 3)
# Convert to list to modify
temp_list = list(tuple)
temp_list.append(4)
# Convert back to tuple
tuple = tuple(temp_list)
print(tuple)  # Output: (1, 2, 3, 4)

