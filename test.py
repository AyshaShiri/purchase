import pandas as pd 
from pandas import concat
movies_df=pd.read_csv(r"C:\\Users\\DELL\\Downloads\\IMDB-Movie-Data.csv",index_col="Title")
movies_df2=pd.read_csv(r"movie2.csv")
print(movies_df.shape)
dupe_df=movies_df.add(movies_df2)
print(dupe_df.shape)
# print(dupe_df.shape)