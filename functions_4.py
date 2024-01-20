# using the length function within a function

marks = [55, 64, 75, 80, 34]

length = len(marks)
print("Length is", length) 

marks_sum = sum(marks)
print("the total marks you got is", marks_sum)

#1. PRINT "LENGTH IS"

#Line 6 is the first line of the code
#it takes the string 'length is' and then calls the function called length
#within length on line 5, it is asking for the length (number of items) in the function marks
# on line 3, marks has 5 items - the length is therefore 5
# so now, on line 6, it will print "Length is 5"

#2. PRINT "THE TOTAL MARKS YOU GOT IS"

# then the code will move to line 9
# when it moves to line 9, it prints the string and then goes on to call the function, marks_sum on line 8
#on line 8, this marks_sum function is basically summing up whatever is defined in the function 'marks' (which is on line 3)
# the sum of marks is 308
# with all of this computed, line 9 now prints out "the total marks you got is 308"