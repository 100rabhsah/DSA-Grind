#Program to Assign grades to a student using Nested If Else

marks = list(map(int, input("Enter marks for all subjects separated by space: ").split()))

max_marks = len(marks) * 100

total = sum(marks)

percentage = (total / max_marks) * 100

if percentage >= 90:
    grade = 'A'
elif 80 <= percentage < 90:
    grade = 'B'
elif 60 <= percentage < 80:
    grade = 'C'
elif 33 <= percentage < 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Total Marks: {total}/{max_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
