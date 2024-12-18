'''WAP to accept basic salary from user and Give 10%DA
   on basic salary,12% HRA on basic salary to employee
   if the salary is more than 50000.calculate total salary.'''


# Accept basic salary input from the user

basic_salary = float(input("Enter the basic salary: "))

# Initialize the DA and HRA 
DA = 0.10  # 10% DA
HRA = 0.12  # 12% HRA

# Check if the salary is more than 50000
if basic_salary > 50000:
    # Calculate DA and HRA
    DA = basic_salary * DA
    HRA = basic_salary * HRA
    
    # Calculate total salary
    total_salary = basic_salary + DA + HRA
    
    # Output the result
    print("Basic Salary=",basic_salary)
    print("Dearness Allowance (DA)=",DA)
    print("House Rent Allowance (HRA)=",HRA)
    print("Total Salary=",total_salary)
else:
    print("Salary is less than 50,000, no DA and HRA ")



