# 2018!!! py 3.7
# Mutable: list, set, dict
# Immutable: int, str, float, tuples
x = "string"
y = [1,2]

print(type(x))

print(type(y))

y.append(3) # lists mutable

print(y) 

y[0] = 7 #el lists mutable

print(y)

print(x + 'ssss')

print(x)
##########
lst = [1,2,3]

z = lst

z.append(8)

print(lst) #### ep! z i lst ocupen el mateix lloc a la memoria

a = 'str'
b=a
print(a)

print(b)
print(a)
a += '5'
print(a)  #epp! a no ha canviat b, Strings are immutables. Same with numbers
print(b)


c = 5
d = c
print(c)
print(d)

c = c+10
print(c)
print(d)# ep! Numbers are immutables