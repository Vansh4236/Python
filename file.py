# Programs to demonstrate File handling in Python:
# 1: Program to read the contents from a text file and display the same on screen.
# 2: Program to count the number of lines, words and characters from a text file.
# 3: Program to read first n lines from a text file
# 4: Program to read lines from a text file and find the length of the longest line.
# 5: Program to read last n lines of a file
# 6: Program to count the frequency of words in a file.
# 7: Program to count lines starting with a word "The"
# 8: Program to replaces all special characters by space
# 9: Program to count occurrences of a word in a file

# Reading and displaying content of the file
filename = "example.txt"
with open(filename, "r") as file:
    content = file.read()
    print(content)

print("********************************************************")
# Counting lines, words, and characters in a file
filename = "example.txt"
with open(filename, "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    
print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
print("********************************************************")

# Reading the first n lines from the file
filename = "example.txt"
n = 5  # change n to the number of lines you want to read
with open(filename, "r") as file:
    for i in range(n):
        print(file.readline().strip())
print("********************************************************")

# Finding the longest line in a file
filename = "example.txt"
with open(filename, "r") as file:
    lines = file.readlines()
    longest_line = max(lines, key=len)
    
print(f"The longest line is: {longest_line.strip()}")
print(f"Length of the longest line: {len(longest_line.strip())}")
print("********************************************************")

# Reading the last n lines from the file
filename = "example.txt"
n = 3  # change n to the number of lines you want to read from the end
with open(filename, "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())
print("********************************************************")

# Counting the frequency of words in a file
filename = "example.txt"
word_freq = {}
with open(filename, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

for word, count in word_freq.items():
    print(f"{word}: {count}")
print("********************************************************")

# Counting lines starting with "The"
filename = "example.txt"
count = 0
with open(filename, "r") as file:
    for line in file:
        if line.startswith("The"):
            count += 1

print(f"Lines starting with 'The': {count}")
print("********************************************************")

# Replacing all special characters with space
import re

filename = "example.txt"
with open(filename, "r") as file:
    content = file.read()
    updated_content = re.sub(r'[^A-Za-z0-9\s]', ' ', content)

print(updated_content)

