import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(
    "/home/harshitlohani/Desktop/Cyno/Practice/Fruits-Uttarakhand/Dataset/Fruits(final).csv"
)

print(df.head())

df=df.drop([2,4,5])
print("After dropping 2,4,5")
print(df.head())
x=df['Fruit']
y=df['Jan (%)']

plt.bar(x, y, label='2x')

plt.title("First Graph")

plt.xlabel("Fruit")
plt.ylabel("Percentage Prroduced in January")

plt.legend()

plt.show()

