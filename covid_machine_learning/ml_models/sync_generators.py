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
        self.data = {}
        self.load_data()

    def load_data(self):
        for x in listdir("../data_sources"):
            if x == "all_data.csv":  # ignore the all_data file
                continue
            with open(f"../data_sources/{x}") as f:
                str_io = StringIO(f.read())
                self.data[x[0:3]] = str_io

    def predict_model(self, country_name: str = "world", key: str = "total_cases", days: int = 28, *,
                      just_last: bool = False):
        if country_name.lower() in ("world", "global", "ot"):
            country_name = "WRL"
        if country_name.upper() not in self.data:
            return None  # data isn't loaded
        str_buffer: StringIO = self.data[country_name.upper()]
        df = pd.read_csv(str_buffer)
        str_buffer.seek(0)  # reset buffer

        return predict_model(df, key, days, just_last=just_last)


if __name__ == "__main__":
    cls = ModelGenerator()
    predicted = cls.predict_model(key="total_vaccinations", just_last=True)
    print(predicted)
