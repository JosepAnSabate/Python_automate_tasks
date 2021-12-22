mylist = ["banana", "cherry", "apple"]

print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist2[0]
print(item)

item2 = mylist2[-1]
print(item2)

## iterant lists
for i in mylist:
    print(i)

# condicional
if "banana" in mylist:
    print("yes")
else: 
    print("no")

## lenght list
print(len(mylist))

## append
mylist.append("pear")
print(mylist)

## append in x position. 1 = index, item
mylist.insert(1, "blueberry")
print(mylist)

## remove items. pop
## remove the list item
item = mylist.pop()
print(mylist)
print(item)

item = mylist.remove("banana") # if the item doesnt exist will give error
print(mylist)
print(item)

## remove all elements of the list
##clearlist = mylist.clear()
##print(clearlist)
##print(mylist)
## reverse order 
reverselist = mylist.reverse()
print(mylist)
print(reverselist) # none
## sorting abcd... or -1, 2, 3...
mylist.sort()
print(mylist)


new_list = reversed(mylist)
print(new_list)

new_list = sorted(mylist)
print(new_list)

mylist = [0] * 5
print(mylist)

mylist2 = [ 1,2,3,4,5]

new_list= mylist + mylist2
print(new_list)

##lists: ordered, mutable, allows duplicate elements
mylist =[ 1,2,3,4,5,6,7,8,9]

a = mylist[1:5] # no afaga ni lelement 0 ni el 5
print(a) # 2,3,4,5

b = mylist[:5] # 0 a 4 el
print(b)
c = mylist[1:] # 1 al final
print(c)

d = mylist[::-1] ## reverse list
print(d)

## Copyng lists
original_list = ["banana", "cherry", "apple"]
list_copy = original_list ## both list refer to the same list  inside the memory
print(list_copy)

list_copy.append("lemon")

print(list_copy)
print(original_list)

## DO IT
list_copy2 = original_list.copy()

print(list_copy2)

list_copy2.append("strawberry")

print(list_copy2)
print("Orgininal list= ",original_list)

## OR
list_copy3 = list(original_list)

print(list_copy3)

list_copy3.append("pineapple")

print("copylist3= ", list_copy3)
print(original_list)

## OR slicing
copiedlist = original_list[:] ## slicing
copiedlist.append("potato")
print("slicedlist= ", copiedlist)
print("original_list= ", original_list)

## 
listz = [1,2,3,4,5,6]

listy = [i*i for i in mylist] # sqaure each element

print("listz: ", listz)
print("listy: ", listy)