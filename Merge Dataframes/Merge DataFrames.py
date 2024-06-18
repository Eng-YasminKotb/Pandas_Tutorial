import pandas as pd
# Merge exactly same as join in tables

print("Primary Merge:\n")
item_weight=pd.DataFrame({
    'item':['Orange','Banana','Apple'],
    'weight':['2','4','3']
})

item_value=pd.DataFrame({
    'item':['Apple','Banana','Orange'],
    'value':['15','20','35']
})

Merged_DataFrame=pd.merge(item_weight, item_value, on='item')
print(Merged_DataFrame)

print("\n\nMerge is just applied on the common keys:\n")# which is the concept of inner join
item_weight=pd.DataFrame({
    'item':['Orange','Banana','Kiwi'],
    'weight':[2,3,4]
})

item_value=pd.DataFrame({
    'item':['Apple','Banana','Orange','Ananas'],
    'value':[15, 20, 35,45]
})
Merged_DataFrame=pd.merge(item_weight, item_value, on='item')
print(Merged_DataFrame)

print("\n\nOuter Join in dataset:\n")
Merged_DataFrame=pd.merge(item_weight, item_value, on="item", how='outer')#Note that 'how' parameter is inner by 'default'
print(Merged_DataFrame)

print("\n\nLeft Join in dataset:\n")
#left_dataFrame is first parameter -->item_weight ['Orange','Banana','Kiwi']
#right_dataFrame is second parameter -->item_value ['Apple','Banana','Orange','Ananas']
#the common between them is+left_dataFrame=['Orange','Banana','Kiwi']
Merged_DataFrame=pd.merge(item_weight, item_value, on="item", how='left')
print(Merged_DataFrame)

print("\n\nRight Join in dataset:\n")
#the common between them is+right_dataFrame=['Apple','Orange','Banana','Anans']
Merged_DataFrame=pd.merge(item_weight, item_value, on="item", how='right')
print(Merged_DataFrame)


print("\n\nUsing indicator parameter at pd.merge():\n")
#To now exactly the item from which dataframe
Merged_DataFrame=pd.merge(item_weight, item_value, on="item", how='outer', indicator=True)
print(Merged_DataFrame)