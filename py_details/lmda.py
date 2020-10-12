# lambda functions
from functools import reduce

lst = [1,2,3,4,5]
d = {'student1': 45, 'student2': 78, 'student3': 12, 'student4': 14, 'student5': 48, 'student6': 43, 'student7': 47, 'student8': 98, 'student9': 35, 'student10': 80}

#ok = list(filter(value = lambda x: x>= 25 and x<=75, d))
#  using filter: to filter out
even = list(filter(lambda x: x>1, lst))



di = {'a': 1, 'b': 2, 'c':12, 'd':9}



# using map : 
evn = list(map( lambda x: x%2==0 , lst))
print(evn)

# reduce : to compute maths 
ev = reduce(lambda x, y: x+y, lst)
print(ev)
