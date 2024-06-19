import pandas as pd

print("\nCreate a dataframe:")
Youtubers_data = {
     'name':["Ahmed Abu_zaid", "Osama Elzero", "Walid Taha", "Eslam Codezilla","Yehia Tech"],
      'age': [36,39,42,38,35],
     'Channel Subscribers':[8000000,1000000,467323,886124,232455]
 }
df=pd.DataFrame(Youtubers_data)

print(df)

print("\n\ncheck the number of dataframe's rows and columns:")
print(df.shape)

print("\n\nStore dataframe's rows and columns in variables:")
rows, columns =df.shape
print(f"{rows}  {columns}")
print("\n\nAnother way to print the whole dataframe:")
print(df.head()) # you an determin the number of sequential ros to print by passing it as a parameter of head()
print(df.head(2))

print("\n\nTo access the last 5 rows of the dataframe:")
#The tail() method returns the last 5 rows if a number is not specified
print(f"{df.tail()} \n")
print(df.tail(2))

print("\n\nTo access a specific sequential rows")
print(df[2:4])
print(df[1:])
print(df[:2])
print(df[:])#all rows

print("\n\nTo Know the names of your columns:")
print(df.columns) ##

print("\n\nTo Know the values of specific column:")
print(df['name'])
print(df.name) #you can also type df.name and get the same output
#the datatype of the column itself is "object" but the dtype of the dataframe itself is "series"
print(type(df['name']))
print(df['Channel Subscribers'])

print("\n\nTo show a specific columns:")
print(df[['Channel Subscribers', 'name']])

print("\n\nTo get the max / min / std in a specific colums:")
print(df['Channel Subscribers'].max());
print(df['Channel Subscribers'].min());
print(df['Channel Subscribers'].std());


print("\n\nTo get a statistic on your data set:")
print(df.describe())

print("\n\nYou can make some selection queries:")
## examples:
print(df[df.age>36]);
print("\n\n")
print(df['Channel Subscribers'] >500000)
print("\n\n")
print(df[['name','age']] [df['Channel Subscribers']==df['Channel Subscribers'].max()])

print("\n\nTo the range of the indexes:")
print(df.index)

print("\n\nUse set_index() method:\n")
print(df.set_index('name'))# Note: it doesn't modify the original dataframe
print(f"\n\n{df}")

##if you wanna affect the original dataframe use inplace=true as a second paramenter in set_index() me

df.set_index('name', inplace=True)
print(f"\n\n{df}")

#then you can access speceific row by the new index which is name in our case Using df.loc['attribute']
print(f"\nAccessing with name:")
print(f"\n{df.loc['Ahmed Abu_zaid']}")


print("\nTo reset the indexes :")
df.reset_index(inplace=True)
print(f"\n{df}")


