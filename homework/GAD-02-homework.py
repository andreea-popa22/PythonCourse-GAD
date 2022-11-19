# declare a list containing the elements 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (in that order)
list1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# display another list in ascending order (the original list must be kept in the same form)
print("--2--")
list2 = list1.copy()
list2.sort()
print(list2)

# display a list sorted in descending order (the original list must be kept in the same form)
print("--3--")
list3 = list1.copy()
list3.sort()
list3.reverse()
print(list3)

# display even numbers from list (using slice ONLY, other method will be considered invalid)
print("--4--")
print(list1[1:2] + list1[3:4] + list1[6:8] + list1[-1:])
print(list2[1::2])

# display odd numbers from list (using slice ONLY, other method will be considered invalid)
print("--5--")
print(list1[0:1] + list1[2:3] + list1[4:6] + list1[8:9])
print(list3[1::2])

# display multiple elements of 3.
print("--6--")
print([list1[2], list1[4], list1[9]])
