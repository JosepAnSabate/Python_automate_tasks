#  Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionaries are changeable, meaning that we can change, 
# add or remove items after the dictionary has been created.

mydict = dict(name="Josep", age =26)

value = mydict["age"]
print(value)

## Mutable, permet afegir o treure items
mydict["email"] = "@easdrhf.com"
print(mydict)


#delete items
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

if "email" in mydict:
    print(mydict["email"])

try: 
    print(mydict["name"])
except:
    print("Error")
# key
for key in thisdict:
    print(key)

#same key
for key in thisdict.keys():
    print(key)
# value
for value in thisdict.values():
    print(value)

# key + value
for key, value in thisdict.items():
    print(key, value)


## Copying dfictionaries
# wrong, modificara als 2 per estar al mateix lloc a la memoria
dict_cpy = thisdict
print(thisdict)

dict_cpy['email'] = ["@uhluo.com"]

print(thisdict)

# CORRECTE
copy2 = dict_cpy.copy()
copy2['telf']= [47868]
print(copy2)
print(dict_cpy)

## Merge dictionaries => update
thisdict.update(mydict)
print(thisdict)