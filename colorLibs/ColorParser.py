from PIL import Image, ImageStat
import math


class ColorParser:
    def __init__(self) -> None:
        pass

    def resize_image(self, image: Image, percent):
        w, h = image.size
        return image.resize((int(w * (percent / 100)), int(h * (percent / 100))), Image.BILINEAR)

    def get_rgb_mean(self, image):
        stat = ImageStat.Stat(image)
        r, g, b = stat.mean
        return [r, g, b]

    def get_brightness(self, rgb):
        return math.sqrt(0.241 * (rgb[0] ** 2) + 0.691 * (rgb[1] ** 2) + 0.068 * (rgb[2] ** 2))

    def get_temperature(self, rgb):
        n = ((0.23881) * rgb[0] + (0.25499) * rgb[1] + (-0.58291) * rgb[2]) / (
            (0.11109) * rgb[0] + (-0.85406) * rgb[1] + (0.52289) * rgb[2]
        )
        cct = 449 * math.pow(n, 3) + 3525 * math.pow(n, 2) + 6823.3 * n + 5520.33
        return cct
