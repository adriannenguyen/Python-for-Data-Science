# Write a for loop the prints out all the element between -5 and 5 using the range function.

for i in range(-4,5):
    print(i)

# Print the elements of the following list: 
# Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.

Genres=['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 

for i in Genres:
    print(i)

# Write a for loop that prints out the following list: 
# squares=['red', 'yellow', 'green', 'purple', 'blue']

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i in squares:
    print(i)

# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
# If the score is less than 6, exit the loop. The list PlayListRatings is given by: 
# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]

while i < len(PlayListRatings) and rating >= 6:
    print(rating)
    i = i + 1
    rating = PlayListRatings[i]

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
# Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while i < len(squares) and squares[i] == "orange":
    new_squares.append(squares[i])
    i = i + 1

print(new_squares)

# Your little brother has just learned multiplication tables in school. 
# Today he has learned tables of 6 and 7. Help him memorise both the tables by printing them using for loop.

print("Multiplicaton table of 6:")
for i in range(11):
    print(f"{i}x6 = {i * 6}")

print("Multiplicaton table of 7:")
for i in range(11):
    print(f"{i}x7 = {i * 7}")

# The following is a list of animals in a National Zoo. 
# Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
# Your brother needs to write an essay on the animals whose names are made of 7 letters. 
# Help him find those animals through a while loop and create a separate list of such animals.

Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
i = 0
new_animals = []

while i < len(Animals):
    animal = Animals[i]
    if len(animal) == 7:
        new_animals.append(animal)
    i = i + 1

print(new_animals)


