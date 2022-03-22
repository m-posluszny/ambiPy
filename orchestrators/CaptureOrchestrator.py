import threading
import queue
from capture.interface import ImageCapturer


class CaptureOrchestrator(threading.Thread):
    def __init__(self, q: queue.Queue, c: ImageCapturer) -> None:
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self.q = q
        self.capturer = c

    def run(self):
        while True:
            image = self.capturer.captureImage()
            self.q.put(image)
