from logging import setLogRecordFactory

poem_lines = open('pelican.txt', 'rt')
# this will open the pelican.txt file and read it as a regular text file

slurp = open('pelican.txt', 'r').read()
# assigned the slurp as a variable. I have opened it and applied the read method
print(slurp)
print(type(slurp))
# the slurp is a string

pelican_as_list = open('pelican.txt', 'r').readlines()
# I have assigned this as a variable, and the readlines method is applied which creates this as a list of lines
print(pelican_as_list)
print(f'Number of lines is', len(pelican_as_list))
# this has printed with the length function displaying the number of lines as 5, as there are 5 items (each line is a item) in the list

for line in open('pelican.txt', 'rt'):
    print(line[:-1])
# this excludes the last item of the line which is \n when read from right to left