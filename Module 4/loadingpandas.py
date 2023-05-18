import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})

# Display the first three rows:
print(df.head(3))

# Obtain column  'a' :
print(df[["a"]])