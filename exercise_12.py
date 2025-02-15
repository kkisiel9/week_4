cheese = ['Cheddar', "Stilton", 'Cornish Yarg']
# this is a list because it is in []
# cheese += 'Oke'
# print(cheese)
# this has added Oke as O,k,e - each letter has been added separately rather than another item in the list

# this is the correct ways to add Oke cheese
# first can append the list and it will add at the end
# cheese.append('Oke')
# print(cheese)
# second way is to use extend operations
# cheese.extend(['Oke'])
# print(cheese)
# can also add via choosing position
# cheese.insert(3, 'Oke')
# print(cheese)

# adding two - can extend the list
cheese.extend(['Oke', 'Brie'])
print(cheese)

tup = 'Hello'
print(len(tup))
# the variable has been defined as the word hello which has 5 characters

tup = 'Hello',
print(len(tup))
print(type(tup))
# this has become a tuple so instead of counting the characters, len is counting number of items in the tuple