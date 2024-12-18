#Q.3)WAP to check whether person can vote or not using function

# Function to check voting eligibility
def vote(age):
    if (age >= 18):
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Input from user
age = int(input("Enter your age: "))

# Call the function to check voting eligibility and display the result
result = vote(age)
print(result)

