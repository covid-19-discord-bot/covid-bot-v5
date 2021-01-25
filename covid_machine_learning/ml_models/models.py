# coding=utf-8
# noinspection SpellCheckingInspection
"""
All credits to Murtaza's Workshop
https://www.youtube.com/watch?v=6CZiz-FLZF0
I simply made PyCharm happier by removing typos
"""
from typing import Optional

import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename='spam.log',
        filemode='w'
    )


logger = logging.getLogger("ml_models-predict")


def predict_model(model_data: Optional[pd.DataFrame] = None, key: str = "total_cases", days: int = 28, *,
                  just_last: bool = False, directory: str = "../data_sources"):
    # load data
    if model_data is None:
        model_data = pd.read_csv(f"{directory}/WRL_data.csv")
    data = model_data[["index", key]]
    data = data.dropna()  # drop all rows with NaN values
    if len(data) == 0:
        return

    # prepare data
    logger.info("Preparing data...")
    x = np.array(data["index"]).reshape(-1, 1)
    y = np.array(data[key]).reshape(-1, 1)

    logger.info("Finding best feature...")
    max_accuracy = [0, 0]
    for i in range(2, 6):
        # prepare PolynomialFeature
        poly_feature = PolynomialFeatures(degree=i)
        a = poly_feature.fit_transform(x)

        # training data
        model = LinearRegression()
        model.fit(a, y)
        ac = model.score(a, y)
        if ac > max_accuracy[1]:
            max_accuracy[0] = i
            max_accuracy[1] = ac
        logger.debug(f"Accuracy is {ac} on degree {i}")

    # prepare PolynomialFeature
    logger.info("Preparing best feature...")
    poly_feature = PolynomialFeatures(degree=max_accuracy[0])
    x = poly_feature.fit_transform(x)

    # training data
    logger.info("Training model...")
    model = LinearRegression()
    model.fit(x, y)

    # prediction
    logger.info("Predicting...")
    final_day = len(data["index"])  # last day in the dataset

    # return
    if just_last:
        return int(model.predict(poly_feature.fit_transform([[final_day + days]])))
    else:
        x1 = np.array(list(range(1, final_day + days))).reshape(-1, 1)
        y1 = model.predict(poly_feature.fit_transform(x1))
        return y1


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    z = predict_model(directory="/home/dustin/PycharmProjects/covid_bot_v5/covid_machine_learning/data_sources")
    print(z)
