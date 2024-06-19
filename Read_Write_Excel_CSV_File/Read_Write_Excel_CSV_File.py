import pandas as pd
print("Dealing with CSV File:\n")
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
    'eps':["not available ","n.a."],
    'revenue':["not available","n.a.",-1],
    'price':["not available ","n.a.",-1],
    'people':["not available ","n.a."]
}
               )
print(f"{df}\n\n")

#Write to csv file
df.to_csv("new.csv")
print(f"{df}\n\n")

#Remove indexes
df.to_csv("new.csv",index=False)#if you open the file in your excel application ,you'll see the affect

#To show your colums
print(f"{df.columns}\n")

#To export specific columns to a new file
# df.to_csv("new.csv",columns=['eps'])
#df.to_csv("new.csv",columns=['eps'],index=False)


#To skip header
df.to_csv("new.csv")

print('#'*100)
print(f"\nDealing with excel File\n")

df=pd.read_excel("stock_data.xlsx")
print(f"{df}\n\n")

#Use of converters argument in read_excel()
def convert_people_cell(cell):
    if cell=='n.a.':
        return 'sam walton'
    return cell

def convert_eps_cell(cell):
    if cell=='not available ':
        return None
    return cell
def convert_revenue_cell(cell):
    if cell=='not available':
        return None
    return cell

def convert_price_cell(cell):
    if cell=='n.a.':
        return None
    return cell

df=pd.read_excel("stock_data.xlsx",converters={
    'people':convert_people_cell,
    'eps':convert_eps_cell,
    'price':convert_price_cell,
    'revenue':convert_revenue_cell
    })
print(f"{df}\n\n")

df.to_excel('new.xlsx',sheet_name="stocks")

#to control the position of the cells' start in the excel sheet
df.to_excel('new.xlsx',sheet_name="stocks",startrow=1, startcol=2) #excel cells is zero_index

#To ignore indexes
df.to_excel('new.xlsx',sheet_name="stocks",index=False)



item_weight=pd.DataFrame({
    'item':['Orange','Banana','Apple'],
    'weight':['2','4','3']
})

item_value=pd.DataFrame({
    'item':['Apple','Banana','Orange'],
    'value':['15','20','35']
})

with pd.ExcelWriter("2_df_in_1_sheet.xlsx") as writer:
    item_weight.to_excel(writer, sheet_name="item_weight")
    item_value.to_excel(writer, sheet_name="item_value")
