import pandas as pd
import matplotlib.pyplot as plt
import chardet

df19 = pd.read_csv("fifa19.csv", encoding = "iso-8859-1")

df21 = pd.read_csv("fifa21.csv", encoding = "iso-8859-1")

#Replace symbols that were not correctly read
df19.replace({'\x86':'e'}, regex=True, inplace=True)
df19.replace({'\x87':'.'}, regex=True, inplace=True)
df19.replace({'\x82':'.'}, regex=True, inplace=True)
df21.replace({'\x86':'e'}, regex=True, inplace=True)
df21.replace({'\x87':'.'}, regex=True, inplace=True)
df21.replace({'\x82':'.'}, regex=True, inplace=True)
df19.replace({'\x89':'%'}, regex=True, inplace=True)
df21.replace({'\x89':'%'}, regex=True, inplace=True)
df19.replace({'\x9c':'oe'}, regex=True, inplace=True)
df21.replace({'\x9c':'oe'}, regex=True, inplace=True)

#Select player with less than 22 years
df_young = df19[df19.Age < 22]

#Create groups based on potential
df_pot90 = df_young[df_young.Potential > 89]
df_pot85 = df_young[(df_young.Potential > 84) & (df_young.Potential < 90)]
df_pot80 = df_young[(df_young.Potential > 80) & (df_young.Potential < 85)]


print("Pot80 en Fifa19, ", df_pot80.shape[0], "players with average", df_pot80.Overall.mean())
print("Pot85 en Fifa19, ", df_pot85.shape[0], "players with average", df_pot85.Overall.mean())
print("Pot90 en Fifa19, ", df_pot90.shape[0], "players with average", df_pot90.Overall.mean())

# Use name, nationality and age to find the players in Fifa 21
column_names = list(df21.columns)

pot_90_21 = pd.DataFrame(columns = column_names)
for index, row in df_pot90.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    pot_90_21 = pd.concat([pot_90_21, temp])
pot_85_21 = pd.DataFrame(columns = column_names)

for index, row in df_pot85.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    pot_85_21 = pd.concat([pot_85_21, temp])
pot_80_21 = pd.DataFrame(columns = column_names)

for index, row in df_pot80.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    pot_80_21 = pd.concat([pot_80_21, temp])

#Mean increase in overall in the different groups
print("Pot80 en Fifa19, ", pot_80_21.shape[0], "players with average", pot_80_21.OVA.mean(), ", increase of ", pot_80_21.OVA.mean() -  df_pot80.Overall.mean())
print("Pot85 en Fifa19, ", pot_85_21.shape[0], "players with average", pot_85_21.OVA.mean(), ", increase of ", pot_85_21.OVA.mean() -  df_pot85.Overall.mean())
print("Pot90 en Fifa19, ", pot_90_21.shape[0], "players with average", pot_90_21.OVA.mean(), ", increase of ", pot_90_21.OVA.mean() -  df_pot90.Overall.mean())


#plt.hist(df_selected.OVA)
#plt.show()
