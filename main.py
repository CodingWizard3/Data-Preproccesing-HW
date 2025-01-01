import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sb
import numpy as np

matches=pd.read_csv(r'matches.csv')
deliveries=pd.read_csv('deliveries.csv')

print(matches.head())
print(matches.isnull().sum())
matches.drop(["deck"], axis=1, errors='ignore', inplace= True)
matches.dropna(inplace=True)
#heatmap not working
sb.heatmap(matches.isnull(),cmap="spring")
pt.show()

print(deliveries.head())
print(deliveries.isnull().sum())
#heatmap not working
sb.heatmap(deliveries.isnull(),cmap="spring")
pt.show()
# How to join?
matches.drop(["deck"], axis=1, errors='ignore', inplace= True)
deliveries.drop(["deck"], axis=1, inplace= True)
