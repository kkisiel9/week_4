create_file = open('pelican.txt, "x')
filez = open("pelican.txt", "w")

filez.write("A wonderful bird is the pelican\n")
filez.write("His bill holds more than his belican\n")

# the \n is necessary to make sure the text is divided and starts in a new line where relevant
lines = ["He can take in his beak, \n", "Enough food for a week, \n", "but i am damned if I see how the helican, \n"]
filez = filez.writelines(lines)