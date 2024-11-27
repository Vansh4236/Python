# A. myTuple= (10, 20, 30)
# B. yourTuple = (“Pune”, ‘Mumbai’, “Delhi”)
# C. mixTuple= ('Foo',[1,2,3],'True')
# D. nestedTuple=((‘ Wes McKinney’,’ Python for Data Analysis’,’ O’Reilly Media’),
# (‘Mark Lutz’,’ Programming Python’,’ O’Reilly Media’),
# (‘Charles Severance’,’ Python for Everybody’,’ Blumenberg’))
# Use built in methods to perform following operations on the tuple:
# 1) Merge myTuple and yourTuple into ourTuple.
# 2) Convert myTuple into list myList and reverse.
# 3) Unpack yourTuple values into three variables - District, State, and National.
# 4) Display all elements of mixTuple.
# 5) Add 4 into list element of mixTuple
# 6) Perform algebraic operations addition and multiplication on myTuple and yourTuple.
# 7) Access information from nestedTuple and display the information as:
# Name of Author = ‘ Wes McKinney’,
# Name of Book = ’ Python for Data Analysis’,
# Name of Publisher= ’ O’Reilly Media’

myTuple= (10, 20, 30)
yourTuple = ("Pune", 'Mumbai', "Delhi")
mixTuple= ('Foo',[1,2,3],'True')
nestedTuple=(('Wes Mckinney',' Python for Data Analysis','O’Reilly Media'),
            ('Mark Lutz','Programming Python','O Reilly Media'),
            ('Charles Severance',' Python for Everybody','Blumenberg'))

# 1) Merge myTuple and yourTuple into ourTuple.
ourTuple = myTuple + yourTuple
print(f"{ourTuple}")

# 2) Convert myTuple into list myList and reverse.
mylist = list(myTuple)
mylist.reverse()
myTuple = tuple(mylist)
print(f"{myTuple}")

# 3) Unpack yourTuple values into three variables - District, State, and National.
District, State, National = yourTuple
print(f"District : {District}")
print(f"State : {State}")
print(f"National : {National}")

# 4) Display all elements of mixTuple.
print(f"{mixTuple}")

# 5) Add 4 into list element of mixTuple
l = mixTuple[1]
l.append(4)
print(f"{mixTuple}")

# 6) Perform algebraic operations addition and multiplication on myTuple and yourTuple.
addTuple = myTuple + yourTuple
mulTuple = yourTuple * 2
print(f"{addTuple}")
print(f"{mulTuple}")

# 7) Access information from nestedTuple and display the information as:
# Name of Author = ‘ Wes McKinney’,
# Name of Book = ’ Python for Data Analysis’,
# Name of Publisher= ’ O’Reilly Media’

for i in nestedTuple:
    Author , Book , Publisher = i
    print(f"Name of Author = {Author},")
    print(f"Name of Book = {Book},")
    print(f"Name of Publisher= {Publisher}")
