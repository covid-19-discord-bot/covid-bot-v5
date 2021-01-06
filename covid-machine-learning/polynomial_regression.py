# coding=utf-8
# noinspection SpellCheckingInspection
"""
All credits to Murtaza's Workshop
https://www.youtube.com/watch?v=6CZiz-FLZF0
I simply made PyCharm happier by removing typos
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# load data
print("Loading data... ", end="")
data = pd.read_csv("processed_data.csv")
data = data[["id", "cases"]]  # try changing this to be something else
print("done!")


# prepare data
print("Preparing data... ", end="")
x = np.array(data["id"]).reshape(-1, 1)
y = np.array(data["cases"]).reshape(-1, 1)
plt.plot(y, "-m")
print("done!")

print("Finding most accurate degree...")
max_accuracy = [0, 0]
for i in range(2, 4):
    print(f"Trying degree {i}...")
    # prepare PolynomialFeature

    poly_feature = PolynomialFeatures(degree=i)
    x = poly_feature.fit_transform(x)
    print("Features prepared...")

    # training data
    model = LinearRegression()
    print("Fitting model...")
    model.fit(x, y)
    print("Scoring model...")
    ac = model.score(x, y)
    if ac > max_accuracy[1]:
        print(f"This model was most accurate at {ac*100}%")
        max_accuracy[0] = i
        max_accuracy[1] = ac
    else:
        print("This model was not more accurate.")
print(f"Done! Degree {max_accuracy[0]} was most accurate, at {max_accuracy[1]*100}%")

print("Preparing feature... ", end="")
# prepare PolynomialFeature
poly_feature = PolynomialFeatures(degree=max_accuracy[0])
x = poly_feature.fit_transform(x)
print("done!")

# training data
print("Creating and fitting model... ", end="")
model = LinearRegression()
model.fit(x, y)
print("done!")

# prediction
days = 28  # number of days to predict
final_day = 349  # last day in the dataset
print(f"Cases after {days} days: {int(model.predict(poly_feature.fit_transform([[final_day+days]])))}")

# graph the prediction
x1 = np.array(list(range(1, final_day+days))).reshape(-1, 1)
y1 = model.predict(poly_feature.fit_transform(x1))
plt.plot(y1, "--r")
plt.show()
