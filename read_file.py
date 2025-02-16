opening = open("pelican.txt", "r")
file_content = opening.read()
# file has been opened, and a new variable created to store its read contents
print(type(file_content))
# checking data type, it's string
print(file_content)
# contents printed
word_list = file_content.split()
# splitting the str into words/elements with each whitespace and creating a list
print(word_list)

no_lines = word_list.strip()
while no_lines:
    print(no_lines)
    break
