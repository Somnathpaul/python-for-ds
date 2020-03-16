def add(num1, num2):
    print(num1+num2)

add(1,2)

# if the number of arguments are unknown
# importnat
def add2(** arg):
    print(arg["num1"]+ arg["num2"] + arg["num3"])

add2(num1 =10,num2=20,num3=30)

# pass:  to avoid getting an error
def ano(str1):
    pass

