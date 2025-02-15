# write a line of code to create a file handle to open and append to a file called pelican.txt
# append the following line to the file using write method
# append following second line using the write method
# create a list that contains the following lines


# this opens the file in write mode 'w'
output = open('sample_files/pelican.txt','w')


# this is writing a string into the file
# the write method returns the no of characters in the string
pelican_text =output.write ("A wonderful bird is the pelican")
print(pelican_text)

# this writes this string into the file pelican.txt
# \n ensures each string will appear on a new line
pelican_text =output.write ("\nHis bill holds more than his belican")
print(pelican_text)

lines =["He can take in his beak,\n", "Enough food for a week, \n", "But I'm damned if I see how the heilican. \n"]
output.writelines(lines)

# \n required to start a new line and break up the txt - looks neater in display

for line in open('sample_files/pelican.txt', 'r'):
    print(line[0:2])