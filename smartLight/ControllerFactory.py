from . import WizNormalizer
from . import WizSender
from .LightController import LightController


class ControllerFactory:
    @staticmethod
    def get_wiz_controller():
        return LightController(WizNormalizer(), WizSender())
