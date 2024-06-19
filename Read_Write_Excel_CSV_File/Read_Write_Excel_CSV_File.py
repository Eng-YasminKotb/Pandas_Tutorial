import pandas as pd

#Original Dataframe
df=pd.read_csv("Stock_skiprows.csv")
print(f"{df}\n\n")

#Skip rows  using skiprows parameter
df=pd.read_csv("Stock_skiprows.csv",skiprows=1)
print(f"{df}\n\n")

#Skip rows  using header parameter
df=pd.read_csv("Stock_skiprows.csv",header=1)
print(f"{df}\n\n")

#Remove headers by header=None
df=pd.read_csv("stock_data.csv",header=None)
print(f"{df}\n\n")


#Remove headers by header=None then give them a name
df=pd.read_csv("stock_data.csv",header=None,names=["tickers","eps","revenue","price","people"])
print(f"{df}\n\n")


#To show specific number of sequential rows
df=pd.read_csv("stock_data.csv",nrows=2)
print(f"{df}\n\n")


#To cleanup messy data from the file
df=pd.read_csv("stock_data.csv",na_values={
    'eps':["not available","n.a."],
    'revenue':["not available","n.a.",-1],
    'price':["not available","n.a.",-1],
    'people':["not available","n.a."]
}
               )
print(f"{df}\n\n")

#Write to csv file
df.to_csv("new.csv")
print(f"{df}\n\n")

#Remove indexes
df.to_csv("new.csv",index=False)#if you open the file in your excel application ,you'll see the affect

#To show your colums
print(df.columns)

#To export specific columns to a new file
# df.to_csv("new.csv",columns=['eps'])
#df.to_csv("new.csv",columns=['eps'],index=False)


#To skip header
df.to_csv("new.csv")