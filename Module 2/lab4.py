# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 

# a) In the dictionary soundtrack_dic what are the keys ?
print(soundtrack_dic.keys())

# b) In the dictionary soundtrack_dic what are the values ?
print(soundtrack_dic.values())

# The Albums Back in Black, The Bodyguard and Thriller have the following music 
# recording sales in millions 50, 50 and 65 respectively:

# a) Create a dictionary album_sales_dict where the keys are the album name and 
# the sales in millions are the values.

album_sales_dict = {"Back in Black": 50, "The Bodyguard": 50, "Thriller": 65}

# b) Use the dictionary to find the total sales of Thriller:
print(album_sales_dict["Thriller"])

# c) Find the names of the albums from the dictionary using the method keys():
print(album_sales_dict.keys())

# d) Find the values of the recording sales from the dictionary using the method values:
print(album_sales_dict.values())
