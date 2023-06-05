import os

def gradingStudents(grades):
    # Write your code here
    l =[]
    for i in grades :
        if i < 38 :
            l.append(i)
        else :
            x=i
            c=0
            while not (x%5 == 0):
                x+=1
                c+=1
            if c <=2 :
                l.append(x)
            else :
                l.append(i)
    return (l)


grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print ('\n'.join(map(str, result)))

