#WAP to find whether person is eligible to vote or not.

# Input: Age of the person
age = int(input("Enter your age: "))

# Check eligibility and display result
if (age >= 18):
     print("you are eligible for vote,your age is",age)
     
else:
    print("You are not eligible for vote,your age is",age)
