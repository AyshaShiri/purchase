import pandas as pd 
movies_df=pd.read_csv(r"C:\\Users\\DELL\\Downloads\\IMDB-Movie-Data.csv",index_col="Title")
a=movies_df.head()
print(a)
b=movies_df.tail(2)
print(b)
c=movies_df.info()
print(c)
print(movies_df.shape)
dup=movies_df.add(movies_df)
print(dup.shape)
print(movies_df.columns)
movies_df.rename(columns={"Runtime (Minutes)":"Runtime","Revenue (Millions)":"Revenue_Millions"},inplace=True)
print(movies_df.columns)
movies_df.columns=[col.lower() for col in movies_df]
print(movies_df.columns)
print(movies_df.isnull())
print(movies_df.isnull().sum())
#movies_df.dropna(axis=1,inplace=True)
#print(movies_df.isnull().sum())
revenue=movies_df['revenue_millions']
print(revenue.head())
r_mean=revenue.mean()
print(r_mean)
r_new=revenue.fillna(r_mean,inplace=True)
print(movies_df.isnull().sum())
print(movies_df.describe())
print(movies_df['revenue_millions'].describe())
print(movies_df['genre'].value_counts())
print(movies_df['genre'].value_counts().head(10))
#print(movies_df.dtypes())
genre_col=movies_df['genre']
print(type(genre_col))
genre_col2=movies_df[['genre']]
print(type(genre_col))
#print(movies_df.corr())
subset=movies_df[['genre','rating']]
print(subset)
prom=movies_df.loc["Prometheus"]
print(prom)
prom2=movies_df.iloc[1]
print(prom2)
movie_subset1= movies_df.loc['Prometheus':'Sing']
movie_subset2= movies_df.iloc[1:4]
print(movie_subset1)
print(movie_subset2)
condition=(movies_df['director'] == "Ridley Scott")
print(condition.head())
print(movies_df[movies_df['director'] == "Ridley Scott"])
print(movies_df[movies_df['rating'] >= 8.6].head(3))
print(movies_df[(movies_df['director'] == 'Christopher Nolan') | (movies_df['director'] == 'Ridley Scott')].head())
print(movies_df[movies_df['director'].isin(['Christopher Nolan', 'Ridley Scott'])].head())
print(movies_df[
    ((movies_df['year'] >= 2005) & (movies_df['year'] <= 2010))
    & (movies_df['rating'] > 8.0)
    & (movies_df['revenue_millions'] < movies_df['revenue_millions'].quantile(0.25))
])
def rating_function (x):
    if x >= 8.0 :
        return "Good"
    else:
        return "Bad"
movies_df['rating_category']=movies_df['rating'].apply(rating_function)
print(movies_df.head(2))
movies_df['rating_category']=movies_df['rating'].apply(lambda x : 'good' if x >= 8.0 else 'bad')
print(movies_df.head(2))
import matplotlib.pyplot as plt 
import seaborn as sns
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})
plt.scatter(x=movies_df['rating'], y=movies_df['revenue_millions'])
plt.title('Revenue (millions) vs Rating')
plt.xlabel('Rating')
plt.ylabel('Revenue (Millions)')
plt.show()
plt.hist(x=movies_df['rating'],bins=10)
plt.title("Rating")
plt.show()
sns.boxplot(data=movies_df,x=movies_df['rating_category'],y=movies_df['revenue_millions'])
plt.title('Boxplot of Revenue by Rating Category')
plt.show()

