#Task-1. You are tasked with creating a Python program to
# represent vehicles using a class. Each car should have attributes 
# for maximum speed and mileage.

class Vehicle(object):
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Task-2. Update the class with the default color for all vehicles," white".

class Vehicle(object):
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Task-3. Additionally, you need to create methods in the 
# Vehicle class to assign seating capacity to a vehicle.

class Vehicle(object):
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

# Task-4. Create a method to display all the properties of an object of the class.
class Vehicle(object):
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehiclee:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Task-5. Additionally, you need to create two objects of the Vehicle class object that should 
# have a max speed of 200kph and mileage of 50000kmpl with five seating capacities, 
# and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.

# Creating objects of the Vehicle class
vehicle_1 = Vehicle(200, 50000)
vehicle_1.assign_seating_capacity(5)
vehicle_1.displayproperties()

vehicle_2 = Vehicle(180, 75000)
vehicle_2.assign_seating_capacity(4)
vehicle_2.displayproperties()

# You have been recruited by your friend, a linguistics enthusiast, 
# to create a utility tool that can perform analysis on a given piece of text

class analysedText(object):
    
    def __init__ (self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        fmtText = text.lower().replace(".", "").replace("!", "").replace(",","").replace("?", "")

        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = fmtText

        pass 
    
    def freqAll(self):    

        # TODO: Split the text into a list of words  
        wordList = self.fmtText.split(" ")

        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        freqMap = {} 

        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap # return the created dictionary
    
    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0