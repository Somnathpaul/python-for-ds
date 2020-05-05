dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("name :", dict['Name'])
print ("age :", dict['Age'])

student = {}
student['roll'] = 21
student['name'] = 'lucky'

print(student['name'])

# to find the repetition of name in the dict
name = ['jill', 'harry', "jill", 'chunk']
count = {}
for n in name:
    count[n] = count.get(n, 0) + 1
print(count)