# Sets: unordered, mutable, no duplicates
myset  = {1,2,3, 2} # no mira dubplicts
myset0 = {"apple", "banana", "cherry"}

myset1 = {"apple"}
myset2 = set("apple")

print(myset)
print(myset0)

print(myset1)
print(myset2)

# empty set
myset = set()
#myset = {} Creara diccionari

#Mutable
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# discard remove a element
myset.discard(2) # si no troba lelement no dona error, simplement no el troba
print(myset)

#loops
for i in myset:
    print(i)

#condic
if 1 in myset:
    print("yes")

# Union, no duplica 
odds = {1,3,5,7}
evens ={0,2,4,6,8}
primes ={2,3,5,7}

u= odds.union(evens)
print(u)

# intersection, comu als dos sets
o = odds.intersection(primes)
print(o)

# difference
setA = {1,2,3,4,5}
setB = {1,2,323,55}

diff = setA.difference(setB)
print(diff)