from smartLight.interface.Normalizer import Normalizer


from ..interface.Normalizer import Normalizer


class WizNormalizer(Normalizer):
    def __init__(self, bright_scale) -> None:
        self.bright_scale = bright_scale

    def normalize_brightness(self, bright):
        bright = self._range_cut(bright, self.bright_scale)
        return int(self._ratio_scaler(bright, self.bright_scale, (0, 255)))

    def normalize_temperature(self, temp):
        temp = self._range_cut(temp, (1000, 8000))
        return int(self._ratio_scaler(temp, (1000, 8000), (2700, 6500)))
