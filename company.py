'''WAP to create dictionaries for below task
and perform all above operations on it.
each customerID in a company is associated with a customer name.'''

company={
    "customer_name":"Shoaib",
    "customer_id":101
    }

print(company)#printing output

x=company["customer_id"]#storing customer_id grade in x
print("customer_id is",x)#printing customer_id

x=company.get("customer_name")
print("customer name is",x)#printing customer name

#find all the keys present in the dictionary
y=company.keys()
print("the keys present are:",y)

company.update({"customer_name":"Zubair"})#to update
print(company)


company["age"]="20"#adding new dictionary
print(company)

#to remove certain element from the dictionary
company.popitem()
print(company)

#looping over dictionary
for i in company:
    print(i)
    
#to get keys from the dictionary
for i in company.values():
    print(i)

for x,y in company.items():
    print(x,y)
    
#to remove an item at specified index.
company.pop("customer_id")
print(company)






