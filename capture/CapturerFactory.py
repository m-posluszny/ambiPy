from capture import D3dCapture
from . import WinCapturer
from . import D3dCapture


class CapturerFactory:
    @staticmethod
    def get_win_capturer(scale=100):
        return WinCapturer(scale)

    @staticmethod
    def get_win_capturer(scale=100):
        return D3dCapture(scale)
