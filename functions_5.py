
'''Suppose you just atteneded a university exam. 
The marks you obtained in the various subjects are stored in a list like this:

marks = [55, 64, 75, 80, 65]

Get the average of the marks you obtained in the exam. 

Grade A: average is >= 80
Grade B: average >= 60 AND <80
Grade C: average is >= 50 AND <60
Grade F: average is < 50
'''

# First, we need a function to find the average marks

def find_average_marks(marks):
    sum_of_marks = sum(marks) #339
    total_subjects = len(marks) #5
    average_marks = sum_of_marks / total_subjects # takes the above and divides them
    return average_marks # returns the result of 67.8

# Secondly, we need a function that calculates the grade and returns it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 65] 
average_marks = find_average_marks(marks)
print("Your average marks is: ", average_marks) # this is the 'first' line of the code 

grade = compute_grade(average_marks)
print("Your grade is: ", grade)