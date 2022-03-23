from queue import LifoQueue
from collections import deque


class CappedQueue(LifoQueue):
    def __init__(self, maxsize: int = ...) -> None:
        super().__init__(maxsize)

    def _init(self, maxsize):
        self.queue = deque(maxlen=maxsize)

    def _qsize(self):
        length = len(self.queue)
        return 0 if length < 1 else length + 1
