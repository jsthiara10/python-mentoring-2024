# passing multiple arguments
# this piece of code is going to add 2 numbers

def add_numbers(n1, n2):
    result = n1 + n2
    return result # so this function here is going to add two numbers, then print the result. the string in the print statement takes the
                                # result of n1 and n2, and prints it

number1 = 5.4
number2 = 6.7
result = add_numbers(number1, number2) # this line here calls the add_numbers function and passes number1 and number2 as n1 and n2 respectively
                              # as such, these hardcoded numbers will be taken up by the function which then prints the result
print("The sum is", result)


