'''WAP to create dictionaries for below task
and perform all above operations on it.
each student in a school is associated with their grade.'''


student={
    "std_name":"Neha",
    "grade":"A"
    }

print(student)#printing output
x=student["grade"]#storing student grade in x

print("student grade is",x)#printing student grade

x=student.get("std_name")
print("student name is",x)#printing student name

#find all the keys present in the dictionary
y=student.keys()
print("the keys present are:",y)

student.update({"std_name":"Sana"})#to update
print(student)


student["address"]="mumbra"#adding new dictionary
print(student)

#to remove certain element from the dictionary
student.popitem()
print(student)

#looping over dictionary
for i in student:
    print(i)
    
#to get keys from the dictionary
for i in student.values():
    print(i)

for x,y in student.items():
    print(x,y)
    
#to remove an item at specified index.
student.pop("grade")
print(student)





