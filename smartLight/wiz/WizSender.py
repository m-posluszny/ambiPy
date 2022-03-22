from common import force_sync
from pywizlight import wizlight, PilotBuilder, discovery
from common.utils import get_or_create_eventloop
from ..interface.Sender import Sender


class WizSender(Sender):
    def __init__(self, ips=[], discovery=False) -> None:
        self.ips = ips
        self.discovery = discovery

    def configure(self):
        loop = get_or_create_eventloop()
        self.lights = [wizlight(ip) for ip in self.ips]
        if discovery:
            self.lights.extend(
                force_sync(discovery.discover_lights, broadcast_space="192.168.1.255")
            )

    def send_brightness(self, bright):
        print(bright)
        for light in self.lights:
            force_sync(light.turn_on, PilotBuilder(brightness=bright))

    def send_temperature(self, temp):
        for light in self.lights:
            force_sync(light.turn_on, PilotBuilder(colortemp=temp))
