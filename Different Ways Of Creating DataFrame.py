import pandas as pd

#Create dataframe using csv file
print("Using CVS file:\n")
df=pd.read_csv("Youtubers_data.csv")
print(df)

#Create dataframe using excel file
print("\n\nUsing Exel file:\n")
df=pd.read_excel("Youtubers_data.xlsx")
print(df)


#Create dataframe using python dictionary
print("\n\nUsing python dictionary:\n")
Youtubers_data = {
     'name':["Ahmed Abu_zaid", "Osama Elzero", "Walid Taha", "Eslam Codezilla","Yehia Tech"],
      'age': [36,39,42,38,35],
     'Channel Subscribers':[8000000,1000000,467323,886124,232455]
 }

df=pd.DataFrame(Youtubers_data)
print(df)

#Create dataframe using python tuples list
print("\n\nUsing python tuples list:\n")
Youtubers_data = {
    ("Ahmed Abu_zaid",36,8000000),
    ("Osama Elzero",39,1000000),
    ("Walid Taha",42,467323),
    ("Eslam Codezilla",38,886124),
    ("Yehia Tech",35,232455)
 }

df=pd.DataFrame(Youtubers_data,columns=['name','age','Youtubers_data'])
print(df)

#Create dataframe using python list of dictionary
print("\n\nUsing list of dictionary:\n")
Youtubers_data = [
    {"name":"Ahmed Abu_zaid","age":36,"Channel Subscribers":8000000},
    {"name":"Osama Elzero","age":39,"Channel Subscribers":1000000},
    {"name":"Walid Taha","age":42,"Channel Subscribers":467323},
    {"name":"Eslam Codezilla","age":38,"Channel Subscribers":886124},
    {"name":"Yehia Tech","age":35,"Channel Subscribers":232455}
     ]
df=pd.DataFrame(Youtubers_data)
print(df)