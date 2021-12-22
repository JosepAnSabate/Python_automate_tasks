# 2018!!! py 3.7
# Mutable: list, set, dict
# Immutable: int, str, float, tuples


def changeList(li): # lli = x
    li.append(100)

def copyList(li):
    newLst = li[:] # copy of li, es pot fer amb copy() o aixi
    newLst.append(100)
    return newLst

x = [1,2,3]
print(x)

#changeList(x)
#print(x) # quan canviem li canviem x. Lists li=x.

x = copyList(x) # crea una copia, indica nova posicio a la memoria.
print(x) # 100 is not added to the old list

# check if 2 items are the same in memory
list1 =[1,2,3]
list2=list1
print(list1 is list2)

list3 = list1[:]
print(list1 is list3)

print(id(list1), id(list2), id(list3))