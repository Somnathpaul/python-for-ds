# List is a collection which is ordered and changeable. Allows duplicate members.
# It is similar to arrays
# list can include another list inside it

num1 = [0,1,2,3,4,3,6,0]
num2 = [1,9,3,5,2,7,2,9]
str1 = "Hello python 3"

# print(num1, num2)

lang = ['python', 'java', 'js', 'ruby', 'php']
# print values with index numbers: always starting from 0
print(lang[0])

# range function: starts counting from 0
print('range :',range(len(lang)))

# split function on list
strlist = str1.split()
print('splitting sentence into a list: ',strlist)

# print the length of the list
print(len(lang)) # expected 5

# print the last value of the list
print(lang[-1]) # expected: php


# append: add end to the list
lang.append('c++')
print(lang) # expected: ['python', 'java', 'js', 'ruby', 'php', 'c++']

# remove: remove values from list. remove passes string
lang.remove('php')
print(lang) # expected: ['python', 'java', 'js', 'ruby', 'c++']

# insert: insert into any position
lang.insert(2, 'node')
print(lang)

# pop: alternative to remove method. both do the same, but pop passes index number
lang.pop(1)
print(lang) # expected: ['python', 'node', 'js', 'ruby', 'c++']

# reverse: reverse the whole list
lang.reverse()
print(lang) # expected:  ['c++', 'ruby', 'js', 'node', 'python']

# print the list from one position to another postion
print(lang[1:4]) # expected: ['ruby', 'js', 'node']

# print the from one position to the end
print(lang[1:]) # expected: ['ruby', 'js', 'node', 'python']

# print the list from one end postion to another end postion
print(lang[-4: -1]) # expected: ['ruby', 'js', 'node']

# loop through the list: prints the list values one by  one
for x in lang:
    print(x)

# check if the item is present in the list
if 'node' in lang:
    print("true")

# sort
lang.sort()
print(lang)

# sort in decending order
lang.sort(reverse=True)
print(lang)

# spliti9ng a real world email
email = "from:	Deeksha Chaturvedi <deeksha.chaturvedi@generalassemb.ly>"

splitdata = email.split()
print(splitdata)