xfile = open('file.txt')
number_of_lines = 0

for x in xfile:
     number_of_lines = number_of_lines + 1
     print(x)

print('Total number of lines :', number_of_lines)

# read will ignore the blank line
read = xfile.read()
print(read)