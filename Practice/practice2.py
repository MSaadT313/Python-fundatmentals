"""Create a Python program to manage student grades using lists, arrays, tuples, and dictionaries.
Implement functions to add students and grades, calculate averages, and display grades for students and subjects."""
student = ["Saad","fasih","raed","ali"]
Dictionary = {"Saad": 23, "fasih":34, "raed": 334}
grades=[1,5,4,67,8,56,4]


def addStudent(name):
    student.append(name)
def addStudent(name,grade):
    Dictionary[name] = grade
def addgrade(grade):
    grades.append(grade)
def calculateaverage():
    sum = 0
    for grade in grades:
        sum += grade
    print (int(sum/len(grades)))    
def displaygrades():
    for grade in grades:
        print(grade , end = " ")  
    print()         
calculateaverage()
addStudent("raed1",100)
addgrade(76)
displaygrades()
print(Dictionary)
print(grades)