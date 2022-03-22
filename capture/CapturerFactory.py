from . import WinCapturer


class CapturerFactory:
    @staticmethod
    def get_win_capturer():
        return WinCapturer()
