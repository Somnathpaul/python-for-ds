xfile = open('file.txt')
number_of_lines = 0

'''
for x in xfile:
     #number_of_lines = number_of_lines + 1
     #print(x)

print('Total number of lines :', number_of_lines)
'''

'''
# read will ignore the blank line
read = xfile.read()
print(read)
'''

'''
for line in xfile:
     # will remove the extra new line
     line  = line.rstrip()
     if not line.startswith('date:'):
          continue
     print(line)

'''

# enter custom file name from user to read the file
file_name = input('enter the file name: ')
try:
     file = open(file_name)
except:
     print('The file ', file_name, 'cannot be opened')
     quit()

# if the try block can open the file, it would proceed from below
print('File ', file_name, 'opened successfully')
print('Reading file ', file_name, '......')
for line in file:
     line =  line.rstrip()
     print(line)