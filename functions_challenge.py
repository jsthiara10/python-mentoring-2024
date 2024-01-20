'''CHALLENGE:

Create a program to add and multiply 2 numbers

Create 2 functions - add_numbers() and multiply_numbers()

These functions should compute the result and return them to the function call

The results should be printed from outside the function'''


def add_numbers (n1, n2):
    result = n1 + n2
    return result

def multiply_numbers (n3, n4):
    result = n3 * n4
    return result

number1 = 2.5
number2 = 3.5
result = add_numbers(number1, number2)
print ("The sum is", result)


number3 = 4.0
number4 = 2.0
result = multiply_numbers(number3, number4)
print ("The multiplied sum is", result)