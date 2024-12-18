#Q.1)WAP to get factorial of a number using function

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        
        #  factorial of 0 or 1 is 1
        return 1
    
    # Recursive call to calculate factorial
    else:
        return n * factorial(n - 1)  

# Input from user
num = int(input("Enter a number to find its factorial: "))

# Call the factorial function and display the result
fact=factorial(num)
print("The factorial of number is ",fact)






