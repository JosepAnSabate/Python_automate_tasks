#A lambda function can take any number of arguments, 
# but can only have one expression.

#lambda arguments : expression
add10 = lambda x: x + 10
print(add10(5))

# amb una funcio es pot fer el mateix pero amb lambda es més curt

suma = lambda x, y, z : x + y + z
print(suma(5, 6, 2))

points2D = [(1,2), (15,1), (5,-1), (10,4)]

points2D_sorted = sorted(points2D)
points2D_sorted_2 = sorted(points2D, key=lambda x: x[1]) # ordena segons coord Y

print(points2D)
print(points2D_sorted)
print(points2D_sorted_2)

points2D_sorted_3 = sorted(points2D, key=lambda x: x[0] + x[1]) # suma dels dos

print(points2D_sorted_3)


#The map() function executes a specified function for each item in an
#iterable. The item is sent to the function as a parameter.

# map(func, seq)
a =[1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

#The filter() function returns an iterator were the items are filtered through a
#  function to test if the item is accepted or not.
ages = [5, 12, 17, 18, 24, 32]

filt = filter(lambda x: x%2 == 0, ages)  # parells, divisibles x2

print(list(filt))