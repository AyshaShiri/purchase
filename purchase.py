import pandas as pd 
import sqlite3
data={"apples":[3,5,1,2],"oranges":[0,2,6,7]}
purchase=pd.DataFrame(data)
purchase=pd.DataFrame(data,index=['Jane','Robert','Lily','David' ])
print(purchase)
p1=purchase.loc['Jane']
print(p1)
p1=pd.read_csv(r"C:\Users\DELL\Downloads\purchases.csv")
print(p1)
p1=pd.read_csv(r"C:\Users\DELL\Downloads\purchases.csv",index_col=0)
print(p1)
p2=pd.read_json(r"C:\Users\DELL\Downloads\purchases.json")
print(p2)
con=sqlite3.connect(r"C:\Users\DELL\Downloads\database.db")
df=pd.read_sql_query("SELECT * FROM purchases",con)
df1=df.set_index("index",inplace=True)
print(df1)
