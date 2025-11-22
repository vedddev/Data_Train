import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path="F:\\Data sciance\\Project\\02_f1\\circuits.csv"
df=pd.read_csv(path)
print(df.isnull().sum())
print(df.head(10))


country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number of Shows/Movies')
plt.xlabel('Number of Shows/Movies')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_movies.png')
plt.show()



