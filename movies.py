import pandas as pd 
movies_df=pd.read_csv(r"C:\\Users\\DELL\\Downloads\\IMDB-Movie-Data (1).csv",index_col="Title")
movies_df.rename(columns={"Runtime_(Minutes)":"Runtime","Revenue_(Millions)":"Revenue_Millions"},inplace=True)

print(movies_df.columns)