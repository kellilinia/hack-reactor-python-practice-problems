# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    average = sum(values) / len(values)
    if average >= 90:
        return "A"
    elif average <= 89 and average >= 80:
        return "B"
    elif average <= 79 and average >= 70:
        return "C"
    elif average <= 69 and average >= 60:
        return "D"
    else:
        return "F"
