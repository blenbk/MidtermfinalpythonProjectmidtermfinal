# Example with a list (mutable)

my_list = [1, 2, 3, 4, 5]



# Modify the list

my_list[2] = 10

print(my_list)  # Output: [1, 2, 10, 4, 5]



# Add a new element to the list

my_list.append(6)

print(my_list)  # Output: [1, 2, 10, 4, 5, 6]



# Example with a string (immutable)

my_string = "hello"



# Try to modify the string

# This will result in an error: TypeError: 'str' object does not support item assignment

# my_string[0] = 'H'



# Try to append to the string

# This will result in an error: AttributeError: 'str' object has no attribute 'append'

# my_string.append('!')



# Instead, you need to create a new string

new_string = my_string + " world"

print(new_string)  # Output: hello world