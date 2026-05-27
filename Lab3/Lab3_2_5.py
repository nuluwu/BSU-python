## Лабораторная работа 3, Задание 2, Вариант 5

import matplotlib.pyplot as plt
import statsmodels.api as sm

EconomyData = sm.datasets.interest_inflation.load_pandas()
EconomyDF = EconomyData.data
Filtered = EconomyDF[
    (EconomyDF["year"] >= 1980) & (EconomyDF["year"] <= 1990)
]

plt.figure(figsize=(10, 6))

plt.plot(
    Filtered["year"],
    Filtered["Dp"],
    label="Inflation (Dp)",
    color="crimson",
    linewidth=2,
)

plt.plot(
    Filtered["year"],
    Filtered["R"],
    label="Interest Rate (R)",
    color="navy",
    linewidth=2,
)

plt.title("Inflation and Interest Rates Dynamics (1980-1990)")
plt.xlabel("Year")
plt.ylabel("Percentage / Value")
plt.legend()
plt.grid(True)

plt.show()