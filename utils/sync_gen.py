# coding=utf-8
import multiprocessing


def background_processor(queue: multiprocessing.Queue):
    while True:
        item = queue.get()
        if item == "kill":
            return
        return_queue: multiprocessing.connection.Connection = item["return"]
        func, args, kwargs = item["func"], item.get("args", []), item.get("kwargs", {})
        return_value = func(*args, **kwargs)
        return_queue.send(return_value)
