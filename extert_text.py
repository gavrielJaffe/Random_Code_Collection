# the mylist variable represents a duplicate list.
mylist = [5, 3, 5, 2, 1, 6, 6, 4 ,5] # the original input list with repeated elements.

dup = {x for x in mylist if mylist.count(x) > 1}
print(dup)

#To count the number of list elements that were duplicated, you can run
print(len(dup))