"""
    Algorithm: Linear Search
    Author: Shamitha R
    Date: 07/08/2024
"""

# Defining the function for linear search:

def linear_search(list1, target):
    """
        Searches for the value stored in the variable target,
        in the list provided as list1.
        1. list1 : Element to be searched (int)
        2. list2 : List with indexes of searched elements .
    """
    list2 = []
    for i in range(len(list1)):
        # Checking if the element to be searched is present at the current index.
        if list1[i] == target:
            # If the element is found, append the index to the list2.
            list2.append(i)
    return list2

# Defining the function to handle few edge cases.

def input_1(prompt):
    """
        To get valid input (Edge case handling)
        1. prompt : The message to be displayed to the user.
        2. ValueError is an exception that occurs when a function 
           receives an argument of the correct type but an inappropriate value.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid Datatype, Enter an integer.")

# Get valid input for the number of elements in the list.
x = input_1("Enter the number of elements in the list: ")

# Number of elements cannot be negative.
if x < 0:
    print("Number of elements cannot be negative.")
else:
    list1 = []
    for i in range(1, x + 1):
        # Get valid input for the elements in the list.
        y = input_1(f"Enter the elements {i}: ")
        list1.append(y)
        # Get valid input for target value.
    target = input_1("Enter the target value : ")

    # Perform linear search on the list
    result = linear_search(list1, target)

    if result:
        print(f"Target fount at: {result}")
    else:
        # If the target element is not present in the list
        print("Target not found")