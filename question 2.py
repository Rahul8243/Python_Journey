#You are given two variables, a and b. Your task is to print these variables in the following formats:

#With space: Print a and b in a single line, separated by a space, followed by a newline.
#Without newline: Print a and b separated by a space, but do not end the output with a newline.
#With separator: Print a and b separated by a specified separator, followed by a newline.
#Without space: Print a and b in a single line, with no spaces between them, followed by a newline.


# Take inputs
a = input("Enter first value: ")
b = input("Enter second value: ")

# Safely take separator input
sep_input = input("Enter separator (press Enter for none): ")
if len(sep_input) == 0:
    separator = " "  # default separator
else:
    separator = sep_input[0]

########### Output Formats ###########

# With space
print(a, b)

# Without newline
print(a, b, end='')

# With separator
print(a, b, sep=separator)

# Without space
print(a + b)
