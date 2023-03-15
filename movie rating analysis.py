import numpy as np
import pandas as pd
import plotly.express as px
movies = pd.read_csv("movies.dat", delimiter='::')
print(movies.head())
movies.columns=['ID','TITLE','GENRE']
print(movies.head())
ratings=pd.read_csv('ratings.dat',delimiter='::')
print(ratings.head())
ratings.columns=['USER','ID','RATINGS','TIMESTAMP']
print(ratings.head())
data=pd.merge(movies,ratings,on=["ID","ID"])
print(data.head())
ratings=data["RATINGS"].value_counts()
numbers=ratings.index
quantity=ratings.values
fig=px.pie(data,values=quantity,names=numbers)
fig.show()
data2=data.query("RATINGS==10")
print(data2["TITLE"].value_counts().head(10))