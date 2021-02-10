import pandas as pd
import matplotlib.pyplot as plt
import chardet

df19 = pd.read_csv("fifa19.csv", encoding = "iso-8859-1")

df21 = pd.read_csv("fifa21.csv")

df_young = df19[df19.Age < 22]

df_pot = df_young[df_young.Potential > 87]

df_pot.replace({'\x86':'e'}, regex=True, inplace=True)
df_pot.replace({'\x87':'.'}, regex=True, inplace=True)
df_pot.replace({'\x82':'.'}, regex=True, inplace=True)

selected = list(df_pot.Name)

df_selected = df21[df21.Name.isin(selected)]

df_selected.drop(df_selected.loc[df_selected['ID']==224442].index, inplace=True)
df_selected.drop(df_selected.loc[df_selected['ID']==256855].index, inplace=True)

plt.hist(df_selected.OVA)
plt.show()

print(df_pot[df_pot.Name == "P. Pellegri"])
