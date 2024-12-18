'''Q1.create dynamic list where you will ask user to enter 5 elements
in it and perform insert new element and delete an element operation
on it'''

# Create an empty list
dynamic_list = []

# Ask the user to enter 5 elements
for i in range(5):
    element = input(f"Enter element {i + 1}: ")
    dynamic_list.append(element)

# Display the current list
print("Current list:", dynamic_list)

# Perform an insert operation

insert_element = input("Enter the element you want to insert: ")
insert_position = int(input("Enter the position  where you want to insert: "))
dynamic_list.insert(insert_position, insert_element)

# Display the list after insert
print("List after insertion:", dynamic_list)

# Perform a delete operation
delete_element = input("Enter the element you want to delete: ")
if delete_element in dynamic_list:
    dynamic_list.remove(delete_element)
else:
    print(f"Element '{delete_element}' not found in the list.")

# Display the list after deletion
print("List after deletion:", dynamic_list)


