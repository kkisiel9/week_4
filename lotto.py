import random
# import the random module
help(random)
# pulls up the help below about what the module can do

lotto_draw = random.sample(range(1, 50), 6)
# assigned a variable for the lotto numbers. I have called a sample method from the random module which is in the range 1-50 and then asked for 6 items
print(lotto_draw)
print(type(lotto_draw))
# print as a list