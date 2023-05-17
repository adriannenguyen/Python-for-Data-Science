# Come up with a function that divides the first input by the second input:

def div(a, b):
    return a/b

result = div(10, 5)
print(result)

# Use the function con for the following question.
def con(a, b):
    return(a + b)

# Can the con function we defined before be used to add two integers or strings?

output = con(10,5)
print(output)

# Can the con function we defined before be used to concatenate lists or tuples?
output = con([5, 4, 3], [2, 1, 0])
print(output)

# Write a function code to find total count of word `little` in the given string: 

def word_count(string):
    words = []
    words = string.split()
    count = 0
    while True:
        if "little" in words:
            count = count + 1
            words.remove("little")
        else:
            break
    print(f"Total count of 'little': {count}")

string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go."
word_count(string)