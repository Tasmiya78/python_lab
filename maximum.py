#Q.2)WAP to find maximum among two number

#Function to find the maximum of two numbers
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to find the maximum and display the result
max_num = max(num1, num2)
print("The maximum number is", max_num)
