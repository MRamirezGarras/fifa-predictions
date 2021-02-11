import pandas as pd
import matplotlib.pyplot as plt

df19 = pd.read_csv("fifa19.csv", encoding = "iso-8859-1")

df21 = pd.read_csv("fifa21.csv", encoding = "iso-8859-1")

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

df_young = df19[df19.Age < 22]

df_av_65 = df_young[df_young.Overall == 65]
df_av_70 = df_young[df_young.Overall == 70]
df_av_75 = df_young[df_young.Overall == 75]
df_av_80 = df_young[df_young.Overall == 80]

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
