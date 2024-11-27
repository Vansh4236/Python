# A. myList= [10, 40, 50, 20, 30,10,40,10]
# B. yourList = ['saw','small','foxes','he','six']
# Use built in methods to perform following operations on the list:
# 1) Append integer 60 into myList
# 2) Insert 70 on 2nd Position
# 3) Sort myList in ascending and descending order.
# 4) Sort yourList in ascending and descending according to length of strings.
# 5) Add float value 3.5 into yourList.
# 6) Use POP and remove method to remove 3.5
# 7) Create ourList by merging myList and yourList
# 8) Find sum of elements in mylist.
# 9) Find smallest, largest and second largest number in a myList.
# 10) Count occurrences of all element in a list

myList= [10, 40, 50, 20, 30,10,40,10]
yourList = ['saw','small','foxes','he','six']

# 1) Append integer 60 into myList
myList.append(60)
print(f"{myList}")

# 2) Insert 70 on 2nd Position
myList.insert(2,70)
print(f"{myList}")

# 3) Sort myList in ascending and descending order.
myList.sort()
print(f"{myList}")

myList.sort(reverse=True)
print(f"{myList}")

# 4) Sort yourList in ascending and descending according to length of strings.
ascending = sorted(yourList, key=len)
descending = sorted(yourList, key=len, reverse=True)

print(f"Ascending order by length: {ascending}")
print(f"Descending order by length: {descending}")

# 5) Add float value 3.5 into yourList.
yourList.append(3.5)
print(f"{yourList}")

# 6) Use POP and remove method to remove 3.5
yourList.remove(3.5)
print(f"{yourList}")

yourList.append(3.5)
yourList.pop(5)
print(f"{yourList}")

# 7) Create ourList by merging myList and yourList
ourList = myList + yourList
print(f"{ourList}")

# 8) Find sum of elements in mylist.
sum = sum(myList)
print(f"Sum : {sum}")

# 9) Find smallest, largest and second largest number in a myList.
small = min(myList)
large = max(myList)
myList.remove(large)
large_2nd = max(myList)

print(f"Small element : {small}")
print(f"Large element : {large}")
print(f"2nd LArge element : {large_2nd}")

# 10) Count occurrences of all element in a list
print(f"{myList}")
element = []
for i in myList:
    if i not in element:
        element.append(i)

for i in element:
    print(f"{i} : {myList.count(i)}")