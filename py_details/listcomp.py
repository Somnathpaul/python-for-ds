'''
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,4,7,1],
    [2,6,8,0]
]

transpose_matrix = [[row[i] for row in matrix] for i in range(4)]
print(transpose_matrix)
'''

'''
name = '1234'
letters = [ i+"0" for i in name]
print(letters)
'''

'''
################### if ###################
lst  = [i*100 for i in range(50,100) if i%2 == 0]
print(lst)
'''

'''
#################### nested if ###################
lst = [i for i in range(1, 100) if i%2==0 if i%5==0]
print(lst)
'''


#################### if  else  ###################
lst = ["even" if i%2==0 else "odd" for i in range(1,10)]
print(lst)


#################### transpose matrix  ###################

transposed = []
matrix = [
    [1, 2, 3, 4],
    [9, 7, 6, 8]
     ]

for i in range(len(matrix[0])):
    #print(matrix[0])
    #print(i)
    #print("--"*10)
    transposed_row = []

    for row in matrix:
        #print(row[i])
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
print("__"*10)

tr= [ [row[i] for row in transposed] for i in range(len(transposed[0]))]
print(tr)