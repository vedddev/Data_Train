import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


path="F:\\Data sciance\\Project\\03_Gym\\RecGym.csv"
df=pd.read_csv(path)

print(df.isnull().sum())
print(df.head(5))
print(df)
