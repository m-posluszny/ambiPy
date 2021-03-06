import threading
from common.utils import get_fps
from structures.CappedQueue import CappedQueue
from colorLibs.ColorParser import ColorParser
from capture.interface import ImageCapturer


class ImageOrchestrator(threading.Thread):
    def __init__(self, colorQueue: CappedQueue, c: ImageCapturer) -> None:
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self.colorQueue = colorQueue
        self.color = ColorParser()
        self.capturer = c

    def procedure(self):
        image = self.capturer.captureImage()
        rgb = self.color.get_rgb_mean(image)
        bright = self.color.get_brightness(rgb)
        temp = self.color.get_temperature(rgb)
        self.colorQueue.put({"brightness": bright, "colortemp": temp})

    def run(self):
        self.capturer.configure()
        while True:
            self.procedure()
