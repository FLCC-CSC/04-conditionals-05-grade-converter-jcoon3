# Name: Justin Coon
# Date: 09-29-2025
# A program that converts numerical grades into letter grades

# Prints grade converter banner
print("===== Grade Converter =====")

# Assigns the numerical_grade variable user input
numerical_grade = float(input("Enter a numerical grade (1-100): "))

# If clause to check if the grade is > 100 and prints A+ if it is
if numerical_grade > 100:
    print("A+")

# elif clause to check the range 90<=x<=100 and prints A if it is
elif numerical_grade in range(90, 101):
    print("A")

# elif clause to check if the grade is from 80<=x<90 and prints B if it is    
elif numerical_grade in range(80, 90):
    print("B")

# elif clause to check if the grade is from 70<=x<80 and prints C if it is       
elif numerical_grade in range(70, 80):
    print("C")

# elif clause to check if the grade is from 65<=x<700 and prints D if it is        
elif numerical_grade in range(65, 70):
    print("D")

# else clause that prints F if the input is under 65
else:
    print("F")