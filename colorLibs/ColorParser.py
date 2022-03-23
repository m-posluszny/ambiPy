from PIL import Image, ImageStat
import numpy as np
import colour
import math


class ColorParser:
    def __init__(self) -> None:
        pass

    def resize_image(self, image: Image, percent):
        w, h = image.size
        return image.resize((int(w * (percent / 100)), int(h * (percent / 100))), Image.BILINEAR)

    def get_rgb_mean(self, image):
        stat = ImageStat.Stat(image)
        r, g, b = stat.rms
        return [r, g, b]

    def get_brightness(self, rgb):
        return math.sqrt(0.241 * (rgb[0] ** 2) + 0.691 * (rgb[1] ** 2) + 0.068 * (rgb[2] ** 2))

    def get_temperature(self, rgb):
        rgb = np.array(rgb)
        XYZ = colour.sRGB_to_XYZ(rgb / 255)
        xy = colour.XYZ_to_xy(XYZ)
        CCT = colour.xy_to_CCT(xy, "hernandez1999")
        return CCT
