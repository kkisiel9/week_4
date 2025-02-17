# write a line of code to create a file handle to open and append to a file called pelican.txt
# append the following line to the file using write method
# append following second line using the write method
# create a list that contains the following lines

create = open('pelican.txt', 'a')
output = open('pelican.txt', 'w')
# a creates a new file 'a' (if it does not exist it will be created)
# w allows you to write in the file 'write' mode

# this is writing a string into the file
# the write method returns the no of characters in the string
pelican_text =output.write ("A wonderful bird is the pelican")
print(pelican_text)

# \n ensures each string will appear on a new line
# the output.write will write a new line into the file
pelican_text =output.write ("\nHis bill holds more than his belican")
print(pelican_text)

# this will create a list
# output.writelines will add it to the file
lines =["He can take in his beak,\n", "Enough food for a week, \n", "But I'm damned if I see how the heilican. \n"]
output.writelines(lines)

# \n required to start a new line

for line in open('pelican.txt', 'r'):
    print(line[0:2])