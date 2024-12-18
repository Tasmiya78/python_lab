# Q3.WAP to find second smallest element in the list.

#creating a list.
list1=[99,66,14,66,89,78,22]

#Remove duplicate elements by set.
remove_dup=(list(set(list1)))

#print the final list after removing dupliste elements
print("the final list is",remove_dup)

#sorted the list
sorted_list=sorted(remove_dup)

#print the sorted list elements.
print("the sorted list is",sorted_list)

#displaying the second largest elements.
print("the second smallest number is",sorted_list[1])

