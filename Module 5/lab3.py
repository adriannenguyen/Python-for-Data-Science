# In the previous section, we used the wget function to retrieve content from the web server as shown below. 
# Write the python code to perform the same task
import requests
import os

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
r = requests.get(url)
path = os.path.join(os.getcwd(), "Example1.text")

with open(path, "wb") as f:
    f.write(r.content)

