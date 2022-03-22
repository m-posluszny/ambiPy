from . import WizNormalizer
from . import WizSender
from .LightController import LightController


class ControllerFactory:
    @staticmethod
    def get_wiz_controller(ips=[], discovery=False):
        return LightController(WizNormalizer(), WizSender(ips, discovery))
