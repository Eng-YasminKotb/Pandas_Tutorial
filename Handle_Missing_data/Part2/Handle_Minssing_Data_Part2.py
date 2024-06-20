import pandas as pd
import numpy as np
df =pd.read_csv("weather.csv")
print(f"{df}\n\n")

print('-'*100)
#   Replace specific data in your dataframe over all
new_df=df.replace('-99999',np.NaN)
print(f"\n{new_df}\n\n")

print('-'*100)
#   Replace specific multiple data in your dataframe over all Using list

new_df=df.replace(['-99999','99999','-88888'],np.NaN)
print(f"\n{new_df} \n\nNow,It sounds good:)\n\n")

print('-'*100)
#   Replace specific value in a specific column Using dictionary
new_df =df.replace({
    'windspeed': ['-99999','99999'],
    'event': ['No Event','-88888']

},np.NaN)
print(f"\n{new_df}\n\nOk,now let's replace a specific value with another value\n\n")

print('-'*100)

new_df = df.replace({
    'windspeed': {
        '-99999':'not valid windspeed',
        '99999':'not valid windspeed'
    },
    'event':{
        'No Event':'not valid event',
        '-88888':'not valid event'
    }
})
print(f"\n\n {new_df}\n\n Now what about 32 F and '31 C'?\n")

#  Replace with Regular Expression


print('-'*100)

new_df = df.replace('[A-Za-z]',' ',regex=True)
print(f"\n\n {new_df}\n\n It isn't sounds what we want we need to exclude event columns!!\nSo,we have to use dictionary as a parameter in replace()\n\n")

print('-'*100)
new_df = df.replace({
    'windspeed': '[A-Za-z]'
},' ',regex=True)
print(f"\n\n {new_df}\n\n")

print('-'*100)
# Replace list of values with another list of values

Student_data =pd.DataFrame({
    'Name':['Ahmed','Abu_zaid','Mohamed'],
    'degree':['bad','good','excellent'],

}
)
print(f"\n\n{Student_data}\n\n")

Student_data=Student_data.replace(['bad','good','excellent'],['10%','50%','100%'])
print(f"\n\n{Student_data}\n\n")