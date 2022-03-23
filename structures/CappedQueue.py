from queue import LifoQueue
from collections import deque


class CappedQueue(LifoQueue):
    def __init__(self, maxsize: int = ...) -> None:
        super().__init__(maxsize)

    def _init(self, maxsize):
        self.queue = deque(maxlen=maxsize)

    def _put(self, item) -> None:
        return super()._put(item)

    def _get(self):
        return super()._get()

    def _qsize(self):
        length = len(self.queue)
        return 0 if length < 2 else length - 1

    def put(self, item, block=True, timeout=None) -> None:
        super().put(item, block, timeout)
        return
