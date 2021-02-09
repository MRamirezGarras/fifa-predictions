import pandas as pd
import matplotlib.pyplot as plt

df19 = pd.read_csv("fifa19.csv")

df21 = pd.read_csv("fifa21.csv")

df_young = df19[df19.Age < 22]

df_pot = df_young[df_young.Potential > 87]

