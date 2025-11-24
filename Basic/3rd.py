"""
Given the following dictionary of student marks:
marks = {'Arjun': 85, 'Priya': 92, 'Rahul': 78, 'Simran': 65, 'Amit': 88, 'Maya': 55, 'Zara': 98}
Task:

Print all students who scored above 80 (name and mark).

Print the names of students whose mark is below the average (compute average!).

Print the student(s) with the highest marks (if more than one, print all).

"""

# ans:
marks = {'Arjun': 85, 'Priya': 92, 'Rahul': 78, 'Simran': 65, 'Amit': 88, 'Maya': 55, 'Zara': 98}
studentsabove80=[]
studentsbelowavg=[]
maxmarks=max(marks.values())
studentswithmaxmarks=[] 
total=0

for i,j in marks.items():
    if(j>80):
        studentsabove80.append(i)
    total=total+j

avgofmarks=total/(len(marks))

for i,j in marks.items():
    if(j<avgofmarks):
        studentsbelowavg.append(i)

for i,j in marks.items():
    if(j==maxmarks):
        studentswithmaxmarks.append(i)

print(" Name of the students Getting above 80:",studentsabove80)
print(" Name of the students Getting Below Average marks:",studentsbelowavg)
print(" Name of the students Getting Highest marks:",studentswithmaxmarks)


