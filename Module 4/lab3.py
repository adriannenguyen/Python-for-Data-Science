import pandas as pd

# Use a variable q to store the column Rating as a dataframe
q = df[["Rating"]]

# Assign the variable q to the dataframe that is made up of the column Released and Artist:
q = df[["Released", "Artist"]]

# Access the 2nd row and the 3rd column of df:
df.loc[1,2]

# Use the following list to convert the dataframe index df to characters and assign it to df_new; 
# find the element corresponding to the row index a and column 'Artist'. 
# Then select the rows a through d for the column 'Artist'

df_new = df
df_new.index = new_index
df_new.loc["a", "Artist"]
df_new.loc["a":"d", "Artist"]