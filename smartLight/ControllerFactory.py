from . import WizNormalizer
from . import WizSender
from .LightController import LightController


class ControllerFactory:
    @staticmethod
    def get_wiz_controller(ips=[], discovery=False, scale=(0, 255)):
        return LightController(WizNormalizer(scale), WizSender(ips, discovery))
