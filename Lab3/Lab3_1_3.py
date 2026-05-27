## Лабораторная работа 3, Задание 1, Вариант 3

import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

RawData = load_wine(as_frame=True)
DataFrame = RawData.data

DataFrame["Target"] = RawData.target

plt.figure(figsize=(8, 6))

for class_number, class_name in enumerate(RawData.target_names):
    CurrentType = DataFrame[DataFrame["Target"] == class_number]

    plt.scatter(
        CurrentType["alcohol"],
        CurrentType["proline"],
        label = class_name,
    )

plt.title("Wine classification analysis")
plt.xlabel("Alcohol content")
plt.ylabel("Proline content")
plt.legend()

plt.show()