import imp
from smartLight.interface.Normalizer import Normalizer


from ..interface.Normalizer import Normalizer


class WizNormalizer(Normalizer):
    def __init__(self) -> None:
        pass

    def normalize_brightness(self, bright):
        return bright

    def normalize_temperature(self, temp):
        return temp
