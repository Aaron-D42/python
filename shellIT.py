import subprocess

ls = subprocess.run("ls", capture_output=True)

#store full output of ls from subprocess
stored = [ls]

#iterate through ls output
for i in stored:
    result = [i.stdout] #stores results of ls in result and only takes stdout data

for x in result:
    lines = ''.join(map(str, result)) #convert result list to string

#remove bytes 'b' from output
blines = lines.replace("b'", '')

#split the string to remove new line breaks
new_lines = blines.split('\\n')

#create list to store final format
f_ls = []

#iterate through list skipping first entry to avoid 'b'
for y in new_lines[0:]:
 f_ls.append(y) #add y to final list

#more formatting to list
f_ls.remove("'")

#print final list of directory
for p in f_ls:
    print(p)
    #if statement to run files
   #if p == 'strings.py':
    #    subprocess.run(['python', 'strings.py'])
   # else:
    #     print(p)'''

