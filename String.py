# Write a Python program to:
# 1: Create a string made of the first, middle and last character
# 2: Append new string in the middle of a given string
# 3: Create a new string made of the first, middle, and last characters of each input string
# 4: Arrange string characters such that lowercase letters should come first
# 5: Count all letters, digits, and special symbols from a given string
# 6: Find all occurrences of a substring in a given string by ignoring the case
# 7: Calculate the sum and average of the digits present in a string
# 8: Write a program to count occurrences of all characters within a string
# 9: Reverse a given string
# 10: Find the last position of a given substring

# 1. Create a string made of the first, middle, and last character
s = "example"
middle = s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1]
result1 = s[0] + middle + s[-1]
print("1:", result1)

# 2. Append new string in the middle of a given string
original = "hello"
to_append = "world"
middle_index = len(original) // 2
result2 = original[:middle_index] + to_append + original[middle_index:]
print("2:", result2)

# 3. Create a new string made of the first, middle, and last characters of each input string
str1 = "python"
str2 = "coding"
middle1 = str1[len(str1) // 2] if len(str1) % 2 != 0 else str1[len(str1) // 2 - 1]
middle2 = str2[len(str2) // 2] if len(str2) % 2 != 0 else str2[len(str2) // 2 - 1]
result3 = str1[0] + middle1 + str1[-1] + str2[0] + middle2 + str2[-1]
print("3:", result3)

# 4. Arrange string characters such that lowercase letters should come first
s = "PyThOn123"
s = "PyThOn123"
lowercase = ""
others = ""

for char in s:
    if char.islower():
        lowercase += char
    else:
        others += char

result4 = lowercase + others
print("4:", result4)


# 5. Count all letters, digits, and special symbols from a given string
s = "Hello123!@#"
letters = sum(char.isalpha() for char in s)
digits = sum(char.isdigit() for char in s)
special = len(s) - letters - digits
print("5: Letters:", letters, "Digits:", digits, "Special Symbols:", special)

# 6. Find all occurrences of a substring in a given string by ignoring the case
s = "Hello world, hello Python"
occurrences = s.lower().count("hello")
print("6: Occurrences of 'hello':", occurrences)

# 7. Calculate the sum and average of the digits present in a string
s = "abc123xyz"
total = 0
count = 0

for char in s:
    if char.isdigit():
        total += int(char)
        count += 1

average = total / count if count > 0 else 0
print("7: Sum:", total, "Average:", average)

# 8. Count occurrences of all characters within a string
s = "hello world"
char_count = {}  

for char in s:  
    if char in char_count:  
        char_count[char] += 1  
    else:
        char_count[char] = 1  

print("8:", char_count)  

# 9. Reverse a given string
s = "abcdef"
reversed_string = s[::-1]
print("9:", reversed_string)

# 10. Find the last position of a given substring
s = "This is a test string"
substring = "is"
last_position = s.rfind(substring)
print("10: Last position of 'is':", last_position)


