from smartLight.interface.Normalizer import Normalizer


from ..interface.Normalizer import Normalizer


class WizNormalizer(Normalizer):
    def __init__(self) -> None:
        pass

    def normalize_brightness(self, bright):
        return int(self._ratio_scaler(bright, (0, 255), (0, 200)))

    def normalize_temperature(self, temp):
        temp = self._range_cut(temp, (1000, 8000))
        return int(self._ratio_scaler(temp, (1000, 8000), (2700, 6500)))
