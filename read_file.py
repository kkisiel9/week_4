opening = open("pelican.txt", "r").readlines()
# file has been opened, and a new variable created to store its read contents
# checking data type, it's
print(type(opening))
print(opening)
# contents printed

print(f"Number of lines is", len(opening))

for line in opening:
    print(line[:-1])
