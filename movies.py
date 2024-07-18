import pandas as pd 
movies_df=pd.read_csv(r"C:\Users\DELL\Downloads\IMDB-Movie-Data.csv",index_col="Title")
a=movies_df.head()
print(a)
b=movies_df.tail(2)
print(b)
c=movies_df.info()
print(c)
d=movies_df.columns
print(d)
e=movies_df.rename(columns={"Runtime(Minutes)":"Runtime","Revenue (Millions)":"Revenue_Millions"},inplace=True)
print(movies_df.columns)

