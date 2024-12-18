#Q.4)WAP to get table of a number using function

# Function to print the multiplication table of a number
def table(number):
    print("Multiplication table for number:")
    
    # Loop from 1 to 10
    for i in range(1, 11):
        
        print("number", number * i)

# Input from user
num = int(input("Enter a number to get table: "))

# Call the function to print the multiplication table
table(num)
