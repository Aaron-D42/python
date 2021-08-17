text = 'Lines of Test\nLines of Code'

#split the text at every \n and then store in lines as a list
lines = text.split('\n')

#loop through items in lines and add a * for each new line
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)

print(lines)
print(text)

