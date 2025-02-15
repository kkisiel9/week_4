create = open('pelican.txt', 'x')
output = open('pelican.txt', 'w')
# the x creates a new file, the w allows to write to the file
pelican_message = output.write('A wonderful bird is the pelican,\n')
print(pelican_message)
# the output.write will write a new line into the file
pelican_message = output.write('His beak can hold more than his belican.\n')
print(pelican_message)
# this writes another line, under the first line and then a blank line is created underneath
lines = ["He can take it in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

output.writelines(lines)
# this writelines function allows multiple lines to be added