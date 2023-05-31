"""Example 1: RandomUser API"""
from randomuser import RandomUser
import pandas as pd

# create a random user object
r = RandomUser()

# we get a list of random 10 users
some_list = r.generate_users(10)

# get full name
name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

# In this Exercise, generate photos of the random 5 users.
for user in some_list:
    print(user.get_picture())

# To generate a table with information about the users, we can write a function containing all desirable parameters
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)    

get_users()

df1 = pd.DataFrame(get_users())  

"""Example 2: Fruitvice API"""
import requests
import json

# obtain the fruitvice API data using requests.get("url") function
data = requests.get("https://fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, 
# so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)

# Let's see if we can extract some information from this dataframe. 
# Perhaps, we need to know the family and genus of a cherry
cherry = df2.loc[df2["name"] == 'Cherry']
print(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

banana = df2.loc[df2["name"]== "Banana"]
print(banana.iloc[0]["nutritions.calories"])

# Choose any API of your interest and use it to load/extract some information
data2 = requests.get("https://www.adoptapet.com/public/apis/pet_list.html")

# Retrieve results using json.loads() function.
results2 = json.loads(data2.text)

# Convert json data into pandas data frame.
pd.DataFrame(results2)
