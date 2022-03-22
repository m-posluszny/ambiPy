import time


def get_fps(method):
    def fps(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f"{1/(te-ts) if ((te-ts) > 0) else 999} FPS")
        return result

    return fps
