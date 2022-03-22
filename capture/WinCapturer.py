from .interface.ImageCapturer import ImageCapturer
import PIL


class WinCapturer(ImageCapturer):
    def captureImage(self) -> PIL.Image:
        pass
