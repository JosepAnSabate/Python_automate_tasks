## Tuples are used to store multiple items in a single variable.
## Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
## A tuple is a collection which is ordered and unchangeable  and allow duplicate values.
tupla = ("apple", "banana")
## orderes, immutable, allows duplicate elements
tupla1 = ("apple", "banana", ["pear"])
print(type(tupla1))
print(type(tupla1[2]))
print(tupla1[-1])

## This is not posible because tuples are immutable
# tupla1[0] ="apple2"

# loops
for i in tupla1:
    print(i)

#conditionals
if "banana" in tupla1:
    print("yes")
else:
    print('no')



tupla2 = ('a','b', 'c', 'd', 'e', 'b', 'c')

print(tupla2.count('c')) # count c
print(tupla2.index('c')) # position first 'c'

# convert tupla to list and viceversa
my_list = list(tupla2)
print("list: ", my_list)

tupla3 = tuple(my_list)
print("tuple: ", tupla3)

## Slicing with tuples. A very nice way to acces to subparts of the 
## tupla with colons :
a = (1,2,3,4,5,6,7,8,9)

b = a[2:5]
c = a[::2] # every second element
d = a[::-1] # reversing a tuple
print(a)
print(b)
print(c)


# TIME tuples vs lists
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=100000)) ## Tuples more FAST