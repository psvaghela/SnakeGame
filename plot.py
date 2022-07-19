from matplotlib import pyplot as plt
import pandas as pd

d1 = {'alpha':['a','b','c','d','e','f'],'freq':[8,6,12,9,3,5]}
d2 = {'alpha':['a','b','c','d','e','f'],'freq':[6,2,8,10,6,7]}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

#print(df.head())

plt.plot(df1.alpha, df1.freq, label = "First Dataset")
plt.plot(df2.alpha, df2.freq, label = "Second Dataset")
plt.xlabel("Alphabets")
plt.ylabel("Frequency")
plt.title("My First Plot")
plt.legend()

plt.show()