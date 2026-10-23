
# Student Grade Calculator

name = input("Enter student name: ")

number_of_subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(number_of_subjects):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    total += mark

average = total / number_of_subjects

print("\n----- Student Report -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
