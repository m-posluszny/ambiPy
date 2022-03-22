from .interface.ImageCapturer import ImageCapturer
from screeninfo import get_monitors
from common.utils import get_fps
from PIL import Image
import mss


class WinCapturer(ImageCapturer):
    def __init__(self):
        self.capturer = mss.mss()
        self.get_monitor()

    def get_monitor(self):
        for m in get_monitors():
            if m.is_primary:
                self.monitor = {"top": 0, "left": 0, "width": m.width, "height": m.height}

    def captureImage(self) -> Image:
        img_mss = self.capturer.grab(self.monitor)
        img = Image.frombytes("RGB", img_mss.size, img_mss.bgra, "raw", "BGRX")
        return img
