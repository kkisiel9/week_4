filez = open("pelican.txt", "w+")

filez.write("a wonderful bird is the pelican")
filez.write("his bill holds more than his belican")

# the \n is necessary to make sure the text is divided and starts in a new line where relevant
lines = ["he can take in his beak, \n", "Enough food for a week, \n", "but i am damned if I see how the helican, \n"]
filez = filez.writelines(lines)