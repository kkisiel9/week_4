# # Question1
cheese=['Cheddar','Stilton','Cornish Yarg']
cheese += 'Oke'
print(cheese)
# this is incorrect because the correct syntax has not been used
# in this case to add Oke to the end of the list we should:
# cheese =+ ['Oke'] this would insert the item Oke not the letters separately

cheese = ['Cheddar','Stilton','Cornish Yarg']
cheese.append ('Oke')
print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.extend (['Oke', 'Mozarella'])
print (cheese)
# in order to add another cheese item to the end of list .append ()
# to add two cheeses insert .extend using () and [] for list items to be added in quotes


# Question 2
tup='Hello'
print (len(tup))
# this method is requesting the character length of a string
# the string 'hello' has 5 characters

tup='Hello',
print(len(tup))
 # the len method requests the length
 # however as there is a comma after the quotes this creates 'one' element
 # therefore anything inside the quotes is considered as a length of 1 item