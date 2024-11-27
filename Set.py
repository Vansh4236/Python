# 1) Create empty set ‘Engineers’ and ‘Managers’.
# 2) Using input method add elements in ‘Engineers’ and ‘Managers’:
# Engineers={'Jane', 'John', 'Janice', 'Jack'}
# Managers ={'Jane', 'Jack', 'Susan', 'Zack'}
# 3) Display all engineers in this format : “Name of Engineer is --- “ Jane
# 4) Copy all managers and construct a tuple myManagers =('Jane', 'Jack', 'Susan', 'Zack')
# 5) Copy all engineers and construct a list myEngineers ={'Jane', 'John', 'Janice', 'Jack'}
# 6) Add new manager ‘Jenifer’
# 7) Create a third set Engineer_Manager by merging both Engineers and Managers sets.
# 8) Display the name of engineers who are not managers
# 9) Display the name of engineers who also serving as managers. 
# 10) Display the name of person who is either engineer or manager only but not performing both jobs

# 1) Create empty set ‘Engineers’ and ‘Managers’.
Engineers = set()
Managers = set()

# 2) Using input method add elements in ‘Engineers’ and ‘Managers’:
# Engineers={'Jane', 'John', 'Janice', 'Jack'}
# Managers ={'Jane', 'Jack', 'Susan', 'Zack'}

Engineers.add('Jane')
Engineers.add('John')
Engineers.add('Janice')
Engineers.add('Jack')
print(f"{Engineers}")

Managers.add('Jane')
Managers.add('Jack')
Managers.add('Susan')
Managers.add('Zack')
print(f"{Managers}")

# 3) Display all engineers in this format : “Name of Engineer is --- “ Jane
print(f"Name of Engineers are : {Engineers}")
print(f"Name of Managers are : {Managers}")

# 4) Copy all managers and construct a tuple myManagers =('Jane', 'Jack', 'Susan', 'Zack')
myManagers = tuple(Managers)
print(f"Tuple Managers are : {myManagers}")

# 5) Copy all engineers and construct a list myEngineers ={'Jane', 'John', 'Janice', 'Jack'}
myEngineers = list(Engineers)
print(f"List Engineers are : {myEngineers}")

# 6) Add new manager ‘Jenifer’
Managers.add('Jenifer')
print(f"Name of Managers are : {Managers}")

# 7) Create a third set Engineer_Manager by merging both Engineers and Managers sets.
Engineer_Manager = Engineers.union(Managers)
print(f"Name of all Engineers and Managers are : {Engineer_Manager}")

# 8) Display the name of engineers who are not managers
name_of_engineers_who_are_not_managers = Engineers.difference(Managers)
print(f"Name of all Engineers who are not Managers are : {name_of_engineers_who_are_not_managers}")

# 9) Display the name of engineers who also serving as managers.
name_of_engineers_who_also_serving_as_managers = Engineers.intersection(Managers)
print(f"Name of all Engineers who are also Managers are : {name_of_engineers_who_also_serving_as_managers}")

# 10) Display the name of person who is either engineer or manager only but not performing both jobs
name_of_person_who_are_either_engineer_or_manager_but_not_both = Engineer_Manager - name_of_engineers_who_also_serving_as_managers
print(f"name of person who is either engineer or manager only but not performing both jobs : {name_of_person_who_are_either_engineer_or_manager_but_not_both}")