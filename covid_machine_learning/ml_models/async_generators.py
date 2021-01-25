# coding=utf-8
from typing import Union
import numpy
from covid_machine_learning.ml_models.sync_generators import ModelGenerator
import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial


class AsyncModelGenerator(ModelGenerator):
    async def async_load_data(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(ProcessPoolExecutor(1), self.load_data)

    async def async_predict_model(self, country_name: str = "world", key: str = "total_cases", days: int = 28, *,
                                  just_last: bool = False) -> Union[numpy.ndarray, int]:
        loop = asyncio.get_event_loop()
        ret = await loop.run_in_executor(ProcessPoolExecutor(1), partial(self.predict_model, country_name=country_name,
                                                                         key=key, days=days, just_last=just_last))
        return ret
