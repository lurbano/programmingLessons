line = "I am an invisible man."
print(line[3])
char11 = line[10]
print(f'The 11th character is "{char11}"')
print(f"The 11th character is \"{char11}\"")


line = "I am an invisible man."
author = "Ralph Ellison"
outLine = line + " by " + author
print(outLine)

line = "I am an invisible man."
author = "Ralph Ellison"
outLine = '"' + line + '"' + " by " + author
print(outLine)

line = "I am an invisible man."
print('The 11th character is ' + '"' + line[10] + '"')

line = "I am an invisible man."
n = 0
for char in line:
    n = n + 1
    print(n, char)
print(f'There are {n} characters in the string: ' + line)


line = "I am an invisible man."
n = 0
for char in line:
    if (char == 'a'):
        n = n + 1
print(f'There are {n} "a"s in the string: ' + line)

line = "I am an invisible man."
words = line.split(" ")
print(words)

line = "I am an invisible man."
words = line.split("i")
print(words)

line = "I am an invisible man."
words = line.split(" ")
n = 0
for word in words:
    n = n + 1
print(f'There are {n} words in the string: ' + line)


line = "I am an invisible man."
newLine = line.replace("i", "*")
print(newLine)


line = "I am an invisible man."
print(line)
line2 = line.replace("I am", "I'm")
print(line2)
line3 = line.replace("i", "")
print(line3)

line = "I am an invisible man."
line = line.replace(".", '')
print(line)

line = "I am an invisible man."
vowels = "aeiouAEIOU"
for v in vowels:
    line = line.replace(v, '')
print(line)
