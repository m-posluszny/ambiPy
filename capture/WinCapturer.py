from .interface.ImageCapturer import ImageCapturer
from screeninfo import get_monitors
from common.utils import get_fps
from PIL import Image
import mss


class WinCapturer(ImageCapturer):
    def __init__(self, scale):
        super().__init__(scale)
        self.capturer = mss.mss()
        self.get_monitor()

    def get_monitor(self):
        offset = lambda size, idx: int(size * ((1 - (self.scale[idx])) / 2))
        scaled = lambda size, idx: int(size * self.scale[idx])
        for m in get_monitors():
            if m.is_primary:
                self.monitor = {
                    "top": offset(m.height, 1),
                    "left": offset(m.width, 0),
                    "width": scaled(m.width, 0),
                    "height": scaled(m.height, 1),
                }

    def captureImage(self) -> Image:
        img_mss = self.capturer.grab(self.monitor)
        img = Image.frombytes("RGB", img_mss.size, img_mss.bgra, "raw", "BGRX")
        return img
