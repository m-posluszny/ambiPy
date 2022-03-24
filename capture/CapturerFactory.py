from . import WinCapturer


class CapturerFactory:
    @staticmethod
    def get_win_capturer(scale=100):
        return WinCapturer(scale)
