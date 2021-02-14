import pandas as pd
import matplotlib.pyplot as plt

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

#Select players with less than 22 years
df_young = df19[df19.Age < 22]

#Create groups based on overall value
df_av_65 = df_young[df_young.Overall == 65]
df_av_70 = df_young[df_young.Overall == 70]
df_av_75 = df_young[df_young.Overall == 75]
df_av_80 = df_young[df_young.Overall == 80]

#Distribution of potential in the groups
plt.hist(df_av_65.Potential)
plt.title("Av 65")
plt.show()

plt.hist(df_av_70.Potential)
plt.title("Av 70")
plt.show()


plt.hist(df_av_75.Potential)
plt.title("Av 75")
plt.show()

plt.hist(df_av_80.Potential)
plt.title("Av 80")
plt.show()

# Use name, nationality and age to find the players in Fifa 21
column_names = list(df21.columns)

ov_65_21 = pd.DataFrame(columns = column_names)
for index, row in df_av_65.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    ov_65_21 = pd.concat([ov_65_21, temp])

#Use the previous dataframe to extract potential values and store them
pot_list = []
for index, row in ov_65_21.iterrows():
    temp = df_av_65[(df_av_65.Name == row["Name"]) & (df_av_65.Nationality == row["Nationality"]) & (df_av_65.Age == row["Age"] - 2)]
    pot_list.append(temp.Potential)
#Add potential values to the dataframe with fifa 21 values
ov_65_21["Pot_19"] = pot_list

plt.scatter(y = ov_65_21.Pot_19, x = ov_65_21.OVA)
plt.title("Players overall 65")
plt.xlabel("Overall Fifa 21")
plt.ylabel("Potential Fifa 19")
plt.show()

ov_70_21 = pd.DataFrame(columns = column_names)
for index, row in df_av_70.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    ov_70_21 = pd.concat([ov_70_21, temp])

#Use the previous dataframe to extract potential values and store them
pot_list = []
for index, row in ov_70_21.iterrows():
    temp = df_av_70[(df_av_70.Name == row["Name"]) & (df_av_70.Nationality == row["Nationality"]) & (df_av_70.Age == row["Age"] - 2)]
    pot_list.append(temp.Potential)
#Add potential values to the dataframe with fifa 21 values
ov_70_21["Pot_19"] = pot_list

plt.scatter(y = ov_70_21.Pot_19, x = ov_70_21.OVA)
plt.title("Players overall 70")
plt.xlabel("Overall Fifa 21")
plt.ylabel("Potential Fifa 19")
plt.show()


ov_75_21 = pd.DataFrame(columns = column_names)
for index, row in df_av_75.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    ov_75_21 = pd.concat([ov_75_21, temp])

#Use the previous dataframe to extract potential values and store them
pot_list = []
for index, row in ov_75_21.iterrows():
    temp = df_av_75[(df_av_75.Name == row["Name"]) & (df_av_75.Nationality == row["Nationality"]) & (df_av_75.Age == row["Age"] - 2)]
    pot_list.append(temp.Potential)
#Add potential values to the dataframe with fifa 21 values
ov_75_21["Pot_19"] = pot_list

plt.scatter(y = ov_75_21.Pot_19, x = ov_75_21.OVA)
plt.title("Players overall 75")
plt.xlabel("Overall Fifa 21")
plt.ylabel("Potential Fifa 19")
plt.show()

ov_80_21 = pd.DataFrame(columns = column_names)
for index, row in df_av_80.iterrows():
    temp = df21[(df21.Name == row["Name"]) & (df21.Nationality == row["Nationality"]) & (df21.Age == row["Age"] +2)]
    ov_80_21 = pd.concat([ov_80_21, temp])

#Use the previous dataframe to extract potential values and store them
pot_list = []
for index, row in ov_80_21.iterrows():
    temp = df_av_80[(df_av_80.Name == row["Name"]) & (df_av_80.Nationality == row["Nationality"]) & (df_av_80.Age == row["Age"] - 2)]
    pot_list.append(temp.Potential)
#Add potential values to the dataframe with fifa 21 values
ov_80_21["Pot_19"] = pot_list

plt.scatter(y = ov_80_21.Pot_19, x = ov_80_21.OVA)
plt.title("Players overall 80")
plt.xlabel("Overall Fifa 21")
plt.ylabel("Potential Fifa 19")
plt.show()