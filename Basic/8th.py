"""
You have a file called students.txt with the following content:
Alice,85,Computer Science
Bob,72,Mechanical Engineering
Charlie,90,Computer Science
Diana,78,Electronics
Eve,88,Computer Science
Frank,81,Mechanical Engineering
Task:

Read the file and create a list of dictionaries with keys: name, marks, department.

Using Sets: Find all unique departments in the file.

Filter: Print all students from Computer Science department.

Statistics: Calculate the average marks for each department.

Write to a new file: Create a file called top_students.txt that contains only students with marks > 80, in this format:
Name: Alice, Marks: 85, Department: Computer Science
Bonus: Find students who are in both "Computer Science" AND have marks > 85 (using set operations or filter).


"""

# ans:
students = []

# Open file, read each line.
with open('students.txt', 'r') as file:
    for line in file:
        # Remove newlines
        line = line.strip()  
         # Skip empty lines
        if line: 
            # Split line into 3 parts: name, marks, department.
            name, marks, department = line.split(',', 2)
            student_dict = {
                'name': name,
                # Convert marks to int (for calculations).
                'marks': int(marks),
                'department': department
            }
            # Add dictionary to the list.
            students.append(student_dict)

print("Student list:", students)

departments = set()
for s in students:
    departments.add(s['department'])
print("Unique departments:", departments)


print("Students of Computer Science:")
for i in students:
    if i['department']=='Computer Science':
        print("Student name:",i['name'])
        print("Student marks:",i['marks'])

       
for dept in departments:
    dept_marks = []
    for student in students:
        if student['department'] == dept:
            dept_marks.append(student['marks'])
    # Now calculate average marks for this department
    if dept_marks:  # double-check dept is not empty, avoids zero division error
        total = 0
        count = 0
        for mark in dept_marks:
            total += mark
            count += 1
        average = total / count
        print(f"Average marks in {dept}: {average:.2f}")
    else:
        print(f"No students in {dept}")

top_students=[]
for i in students:
    if i['marks']>80:
        student_dict = {
                'name': i['name'],
                'marks': i['marks'],
                'department': i['department']
            }   
        top_students.append(student_dict)

print(top_students)

with open('top_students.txt', 'w') as file:
    for s in top_students:
        line = f"Name: {s['name']}, Marks: {s['marks']}, Department: {s['department']}\n"
        file.write(line)

with open('top_students.txt', 'r') as file:
    for line in file:
        print(line.strip())


for i in students:
    if i['department']=='Computer Science' and i['marks']>85:
        print("Student name:",i['name'])
        print("Student marks:",i['marks'])