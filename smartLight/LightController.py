from .interface.Normalizer import Normalizer
from .interface.Sender import Sender


class LightController:
    def __init__(self, normalizer: Normalizer, sender: Sender) -> None:
        self.normalizer = normalizer
        self.sender = sender

    def set_brightness(self, bright):
        normalized = self.normalizer.normalize_brightness(bright)
        self.sender.send_brightness(normalized)

    def set_temperature(self, temp):
        normalized = self.normalizer.normalize_temperature(temp)
        self.sender.send_temperature(normalized)
