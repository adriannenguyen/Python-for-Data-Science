# What is the value of the variable a after the following code is executed?
a = "1"
print(a)

# What is the value of the variable b after the following code is executed?
b = "2"
print(b)

# What is the value of the variable c after the following code is executed?
c = a + b
print(c)

# Consider the variable d use slicing to print out the first three elements:
d = "ABCDEFG"
print(d[0:3])

# Use a stride value of 2 to print out every second character of the string e:
e = 'clocrkr1e1c1t'
print(e[::2])

# Print out a backslash:
print("\\")

# Convert the variable f to uppercase:
f = "You are wrong"
print(f.upper())

# Convert the variable f2 to lowercase:
f2="YOU ARE RIGHT"
print(f2.lower())

# Consider the variable g, and find the first index of the sub-string snow:
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(g.find("snow"))

# In the variable g, replace the sub-string Mary with Bob:
h = g.replace("Mary", "Bob")
print(h)

# In the variable g, replace the sub-string , with .:
i = g.replace(",", ".")
print(i)

# In the variable g, split the substring to list:
split_string = g.split()
print(split_string)

# In the string s3, find the four consicutive digit character using \d and search() function:
import re

s3 = "House number- 1105"
# Use the search() function to search for the "\d" in the string
match = re.search("\d\d\d\d", s3)

# Check if a match was found
if match:
        print(match.group())
else:
        print("No match")

# In the string str1, replace the sub-string fox with bear using sub() function:
str1= "The quick brown fox jumps over the lazy dog."
new_str1 = re.sub(r"fox", "bear", str1, flags = re.IGNORECASE)
print(new_str1)

# In the string str2 find all the occurrences of woo using findall() function:
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
matches = re.findall(r"woo", str2)
print(matches)
