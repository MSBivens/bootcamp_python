# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def _countdown(num):
    result = []
    for i in range(num,-1,-1):
        result.append(i)
    return result

print(_countdown(5))

# Create a function that will receive a list with two numbers. Print the first value and return the second.
def _Print_and_Return(list):
    print(list[0])
    return list[1]

print(_Print_and_Return([1,2]))

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def _First_Plus_Length(list):
    return list[0] + len(list)

print(_First_Plus_Length([1,2,3,4,5]))

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
def _Values_Greater_than_Second(list):
    if len(list) < 2:
        return False
    result = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            result.append(list[i])
    print(len(result))
    return result

print(_Values_Greater_than_Second([5,2,3,2,1,4]))
print(_Values_Greater_than_Second([3]))

# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def _This_Length_That_Value(size,value):
    result = []
    for i in range(0,size):
        result.append(value)
    return result

print(_This_Length_That_Value(4,7))
print(_This_Length_That_Value(6,2))