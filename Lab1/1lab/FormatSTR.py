  
   #example
#age = 36
#txt = "My name is John, I am " + age
#print(txt)



#example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



