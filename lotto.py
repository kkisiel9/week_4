import  random
# importing the random module
new_set = set()
# creating a new variable/set which is empty. I am choosing a set because it allows no duplicates
while len(new_set) < 7:
    # while loop, while the number of elements in my set is lower than 7, i want it to iterate and get me a new int
    new_set.add(random.randint(1, 51))
    # here I am adding new ints to my set with every iteration
    # print(type(new_set))
    if len(new_set) == 6:
        # only when the amount of elements is equal to 6, i print the set
        print(new_set)