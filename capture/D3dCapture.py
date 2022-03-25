from .interface.ImageCapturer import ImageCapturer
from PIL import Image
import d3dshot


class D3dCapture(ImageCapturer):
    def __init__(self, scale):
        super().__init__(scale)
        self.capturer = d3dshot.create()

    def configure(self):
        self.capturer.capture()

    def captureImage(self) -> Image:
        img = None
        while img is None:
            img = self.capturer.get_latest_frame()
        return img
