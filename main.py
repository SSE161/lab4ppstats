import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cars.csv")



plt.hist(df["eng_size"])
plt.xlabel("eng_size")
plt.ylabel("amount of cars")
plt.show()
plt.hist(df["horsepwr"])
plt.xlabel("horsepwr")
plt.ylabel("amount of cars")
plt.show()

x = df["eng_size"]
y = df["horsepwr"]
plt.scatter(x, y)
plt.xlabel("eng_size")
plt.ylabel("horsepwr")
plt.show()

print(df["eng_size"].describe())
print(df["horsepwr"].describe())
