# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    if len(values) == 0:
        return None
    largest = values[0]
    second_largest = 0
    for value in values:
        if value < largest and value > second_largest:
           second_largest = value

        elif value > largest:
            second_largest = largest
            largest = value
    return second_largest
