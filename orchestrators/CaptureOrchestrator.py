import threading
import queue
from common.utils import get_fps
from capture.interface import ImageCapturer


class CaptureOrchestrator(threading.Thread):
    def __init__(self, q: queue.Queue, c: ImageCapturer) -> None:
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self.q = q
        self.capturer = c

    def procedure(self):
        image = self.capturer.captureImage()
        self.q.put(image)

    def run(self):
        while True:
            self.procedure()
