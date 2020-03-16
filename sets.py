# A set is a collection which is unordered and unindexed

lang = {"php", "java", "node", "python", "ruby"}

# check if the value is present in the tuple
if "php" in lang:
    print("true")

# to print every value one at a time
for x in lang:
    print(x)

# to add values to the set
lang.add('js')
print(lang)

# remove item from set
lang.remove("php")
print(lang)

# clear set will give us only blank set
lang.clear()
print(lang)

# delete set will delete the whole set
del lang
# print(lang)