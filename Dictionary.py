# Create a dictionary myWallet by reading the elements and get() method.
# myWallet={'Diary': 1, 'CCards': 2, 'DCards': 2, 'VCards': 5}
# Perform following operations on myWallet dictionary:
# 1) A new credit card is added in myWallet
# 2) Check that any Photograph available in myWallet or not in True or False output.
# 3) Add four Photographs in myWallet.
# 4) Remove Photographs using del() method and pop() method.
# 5) Represent the particulars of dictionary in the form of tuple.
# 6) Sort the item of myWallet in ascending order based on items.
# 7)Sort the items of myWallet in the ascending order based on item quantity

myWallet={'Diary': 1, 'CCards': 2, 'DCards': 2, 'VCards': 5}
# 1) A new credit card is added in myWallet
myWallet['CCards'] += 1
print(f"{myWallet}")

# 2) Check that any Photograph available in myWallet or not in True or False output.
if 'Photograph' in myWallet:
    print("True")
else:
    print("False")

# 3) Add four Photographs in myWallet.
myWallet['Photographs'] = 4
print(f"{myWallet}")

# 4) Remove Photographs using del() method and pop() method.
del myWallet['Photographs']
print(f"{myWallet}")
myWallet['Photographs'] = 4
myWallet.pop('Photographs')
print(f"{myWallet}")

# 5) Represent the particulars of dictionary in the form of tuple.
myWallet_tuple = tuple(myWallet.items())
print(f"{myWallet_tuple}")

# 6) Sort the item of myWallet in ascending order based on items.
myWallet_sorted_items = sorted(myWallet.items())
print(f"{myWallet_sorted_items}")

# 7)Sort the items of myWallet in the ascending order based on item quantity
myWallet_sorted_keys = sorted(myWallet.items(),key = lambda x:x[1])
print(f"{myWallet_sorted_keys}")