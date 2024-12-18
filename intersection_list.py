#Q4. perform intersection operation on list.
list1=[22,44,66,33,45]#creating a list1
list2=[44,33,12,34,45]#creating a list2


#printing the list1 and list2 before intersection.
print(list1)
print(list2)

#Finding the intersection using sets.
intersection=list(set(list1)& set(list2))

#Display the result after intersection.
print("List intersection is",intersection)
