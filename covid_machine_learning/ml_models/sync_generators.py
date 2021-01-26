# coding=utf-8
from covid_machine_learning.ml_models.models import predict_model
import logging
import pandas as pd
from os import listdir
from io import StringIO


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename='spam.log',
        filemode='w'
    )


class ModelGenerator:
    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def predict_model(self, country_name: str = "world", key: str = "total_cases", days: int = 28, *,
                      just_last: bool = False):
        if country_name.lower() in ("world", "global", "ot"):
            country_name = "WRL"

        return predict_model(country_name, key, days, just_last=just_last)


if __name__ == "__main__":
    cls = ModelGenerator()
    predicted = cls.predict_model(key="total_vaccinations", just_last=True)
    print(predicted)
