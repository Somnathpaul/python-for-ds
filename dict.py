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

# a program to find the repetition of words in a sentence
define_python= "In Python, a function is a group of related statements that performs a specific task.Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable."
hash_map={}
lst = define_python.split()
print(lst)
for i in lst:
    hash_map[i] = hash_map.get(i,0) +1
print(hash_map)

names = {'jack': 1, 'brad': 2, 'jill': 3}
for n in names:
    # n prints names key
    # names[n] prints number values
    print(n, names[n])

# built in functions
print(names.keys())
print(names.values())

# special case for loop for dict
for k,v in names.items():
    print(k,v)