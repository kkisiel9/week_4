# import random module to assist in generating random numbers
import random
help(random)
# help function to find out what is in the library called random
# under the documentation for integers
# there a various random methods
# python documentation
# random.randint returns a random int/number
# random.sample - used for random sampling without replacement
# to choose a sample from a range of integers use a range () object as an argument
# insert the number range in this case 1-50 and key as 6
# by using a set the generated numbers will always be unique as sets in python are unique
# while loop to return generated numbers as a set

lotto_numbers=set()
while len(lotto_numbers) < 6:
    lotto_numbers.add(random.randint(1,49))

print(lotto_numbers)

# numbers=random.sample(range(1,50),6)
# print (numbers)
# # this prints a list
#
# numbers_set=set(numbers)
# print(numbers_set)
# change output to set not list -sets in Python are unique
# sets are unordered and unique unlike lists
# this appears to be the best data structure for this script
# the script is generating 6 unique random numbers between 1-50