import asyncio
import time
import yaml
from PIL import Image


def get_time(method):
    def timer(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f"{(te-ts)} s - {method.__name__}")
        return result

    return timer


def get_fps(method):
    def fps(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("")
        print(f"{1/(te-ts) if ((te-ts) > 0) else 999:.2f} FPS - {method.__name__}")
        return result

    return fps


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()
        else:
            raise ex


def force_sync(method, *args, **kwargs):
    res = method(*args, **kwargs)
    if asyncio.iscoroutine(res):
        return get_or_create_eventloop().run_until_complete(res)
    return res


def force_sync_decorator(method):
    def wrapper(*args, **kwargs):
        return force_sync(method, *args, **kwargs)

    return wrapper


def yaml_load(file):
    print(file)
    with open(file, "r") as stream:
        return yaml.full_load(stream)
