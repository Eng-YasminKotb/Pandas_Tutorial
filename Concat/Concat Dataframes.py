import pandas as pd

df1=pd.DataFrame({
    'name':['Ahmed','Muhammed','Yasmin'],
    'age':[22, 21, 23]
})

df2=pd.DataFrame({
    'name':['Saif','Anas','Braa'],
    'age':[29, 24, 26]
})


#concat([df1, df2])
print("Primary Concatenation:\n")
print(pd.concat([df1, df2]))

#To make the concatnated dataframes with sequential indexes
print("\n\nTo make the concatnated dataframes with sequential indexes:\n")
print(pd.concat([df1, df2], ignore_index=True))#ignore_index parameter False by default


print("\n\nUsage of keys parameter at .concat() method:\n")
print(pd.concat([df1, df2], keys=['First_Group','Second_Group']))
#Don't provide ignore_index parameter to get the output of keys parameter

print("\n\nAccessing(Indexing) the previous dataframes with the new keys:\n")
Concatenated_DataFrame=pd.concat([df1, df2], keys=["First_Group","Second_Group"])
print(f"{Concatenated_DataFrame.loc["First_Group"]}\n")
print(f"{Concatenated_DataFrame.loc["Second_Group"]}\n")
#print(pd.concat([df1, df2], axis=1))

#Vertical  DataFrame Concatenation
print("\n\nVertical DataFrame Concatenation:\n")
item_weight=pd.DataFrame({
    'item':['Orange','Banana','Apple'],
    'weight':['2','4','3']
})

item_value=pd.DataFrame({
    'item':['Apple','Banana','Orange'],
    'value':['15','20','35']
})

print(pd.concat([item_value,item_weight], axis=1))

#To match the order of the two DataFrames Use "index" parameter at pd.DataFrame()
print("\n\nTo match the order of the two DataFrames:\n")
item_weight=pd.DataFrame({
    'item':['Orange','Banana','Apple'],
    'weight':['2','4','3']
}, index=[0,1,2])

item_value=pd.DataFrame({
    'item':['Apple','Banana','Orange'],
    'value':['15','20','35']
},index=[2,1,0])

print(pd.concat([item_value,item_weight], axis=1))