# opens the file and reads it as a string
# this slurps the entire contents of the file
# it is a string
birds = open('pelican.txt', 'r').read()
print(birds)
print (type(birds))

# this turns it into a list of lines by using the readlines method
bird_txt = open('pelican.txt').readlines()
print(bird_txt)
print(type(bird_txt))

# len counts the number of lines
print(f'Number of lines', len('bird_txt'))

# this for loop iterates through each line in the file
# [:-1] this does not include the last item of the list \n from counting from right to left
for line in open('pelican.txt', 'r'):
    print(line[:-1])