# Exam Problem: Student Grading

# Write a Python program that calculates the final grades for a class of students.
# The program should ask the user to enter the number of students and the weightage
# (in percentages) of three exams: Exam 1, Exam 2, and Exam 3. Then, for each student,
# it should prompt the user to enter the scores for these exams. Finally, the program
# should calculate and display the final grades for each student.

# Grading scale:
#   - Exam 1: 30%
#   - Exam 2: 40%
#   - Exam 3: 30%

# Example output:
#   Enter the number of students: 3
#   Enter the weightage of Exam 1 (in %): 30
#   Enter the weightage of Exam 2 (in %): 40
#   Enter the weightage of Exam 3 (in %): 30
#
#   Student 1:
#     Enter the score for Exam 1: 85
#     Enter the score for Exam 2: 90
#     Enter the score for Exam 3: 80
#     Final grade: 86.5
#
#   Student 2:
#     Enter the score for Exam 1: 70
#     Enter the score for Exam 2: 80
#     Enter the score for Exam 3: 75
#     Final grade: 76.0
#
#   Student 3:
#     Enter the score for Exam 1: 95
#     Enter the score for Exam 2: 85
#     Enter the score for Exam 3: 90
#     Final grade: 89.5

# Function to calculate the final grade
def calculate_final_grade(exam1, exam2, exam3, weightage1, weightage2, weightage3):
    total_weightage = weightage1 + weightage2 + weightage3
    weighted_exam1 = (exam1 * weightage1) / 100
    weighted_exam2 = (exam2 * weightage2) / 100
    weighted_exam3 = (exam3 * weightage3) / 100
    final_grade = (weighted_exam1 + weighted_exam2 + weighted_exam3) / total_weightage * 100
    return final_grade

# Main program
num_students = int(input("Enter the number of students: "))
weightage1 = int(input("Enter the weightage of Exam 1 (in %): "))
weightage2 = int(input("Enter the weightage of Exam 2 (in %): "))
weightage3 = int(input("Enter the weightage of Exam 3 (in %): "))

for i in range(1, num_students + 1):
    print(f"\nStudent {i}:")
    exam1 = float(input("  Enter the score for Exam 1: "))
    exam2 = float(input("  Enter the score for Exam 2: "))
    exam3 = float(input("  Enter the score for Exam 3: "))

    final_grade = calculate_final_grade(exam1, exam2, exam3, weightage1, weightage2, weightage3)
    print(f"  Final grade: {final_grade:.1f}")
