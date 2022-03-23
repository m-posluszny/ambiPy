from .interface.Normalizer import Normalizer
from .interface.Sender import Sender


class LightController:
    def __init__(self, normalizer: Normalizer, sender: Sender) -> None:
        self.normalizer = normalizer
        self.sender = sender
        self.config = {}

    def configure(self):
        self.sender.configure()

    def set_brightness(self, bright):
        normalized = self.normalizer.normalize_brightness(bright)
        self.config["brightness"] = normalized

    def set_temperature(self, temp):
        normalized = self.normalizer.normalize_temperature(temp)
        self.config["colortemp"] = normalized

    def apply(self):
        self.sender.send(self.config)
        self.clear()

    def clear(self):
        self.config = {}
