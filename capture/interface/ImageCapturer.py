from PIL import Image


class ImageCapturer:
    def __init__(self, scale):
        self.scale = scale

    def configure(self):
        pass

    def captureImage(self) -> Image:
        pass
