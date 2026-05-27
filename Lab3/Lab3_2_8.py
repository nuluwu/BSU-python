## Лабораторная работа 3, Задание 2, Вариант 8

import matplotlib.pyplot as plt
import statsmodels.api as sm

NileData = sm.datasets.nile.load_pandas()
NileDF = NileData.data
Filtered = NileDF[(NileDF["year"] >= 1890) & (NileDF["year"] <= 1910)]

plt.figure(figsize=(10, 5))

plt.plot(
    Filtered["year"],
    Filtered["volume"],
    color="blue",
    marker="o",
)

plt.title("Nile river flow dynamics (1890-1910)")
plt.xlabel("Year")
plt.ylabel("Volume")
plt.grid(True)

plt.show()