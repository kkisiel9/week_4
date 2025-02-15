bird = open('sample_files/pelican.txt', 'rt')
# rt is used to open txt files only not binary
# opens the file in read mode 'rt'

# opens the file and reads it as a string
birds = open('sample_files/pelican.txt').read()
print(birds)
# this prints out a string as it has been stored in a variable

# opens the file, splitlines splits it into a list of lines
bird_txt = open('sample_files/pelican.txt').read().splitlines()
birds_as_list = open('sample_files/pelican.txt', 'r').read().splitlines()
print(f"\n{birds_as_list}")

# this for loop iterates through each line in the file
for line in open('sample_files/pelican.txt', 'r'):
    print(line[:-1])