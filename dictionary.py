# dictionary is python is similar to json data

# A dictionary is a collection which is unordered, changeable and indexed

lang = {
    "name" : "python",
    "type" : "programming",
    "used": "ds",
    "developed": "1980",
    "execute_syntax": "python3 dictionary.py"

}

# accessing the data
print(lang["name"])

# update a data:
lang["developed"] = "1980s"
print(lang)

# add data 
lang["developed_by"] = "Guido van Rossum"
print(lang)

# additional documentation : https://www.w3schools.com/python/python_dictionaries.asp