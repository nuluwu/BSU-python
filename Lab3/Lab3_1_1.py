## Лабораторная работа 3, Задание 1, Вариант 1

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

RawData = load_iris(as_frame = True)
DataFrame = RawData.data

DataFrame["Target"] = RawData.target

plt.figure(figsize = (8, 6))

for class_number, class_name in enumerate(RawData.target_names):
    SubTable = DataFrame[DataFrame["Target"] == class_number]
    
    plt.scatter(
        SubTable["sepal length (cm)"],
        SubTable["sepal width (cm)"],  
        label = class_name,
    )

plt.title("Iris sepal sizes")
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.legend()

plt.show()