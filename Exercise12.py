cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# to add to this list, two things can be done
cheese.append("Oke")
# adds just one element
cheese.extend(("Brie", "Gruyere"))
# adds a tuple
print ((type(cheese)))
print(cheese)

# if [tup = "Hello",] then tup is a tuple with one element in it, because it has the comma added
# when tup = "hello", it's just a string variable
tup = "Hello",
print(len(tup))