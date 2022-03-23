from common import force_sync
from pywizlight import wizlight, PilotBuilder, discovery
from common.utils import get_fps, get_or_create_eventloop, get_time
from ..interface.Sender import Sender
import asyncio


class WizSender(Sender):
    def __init__(self, ips=[], discovery=False) -> None:
        self.ips = ips
        self.discovery = discovery

    def configure(self):
        get_or_create_eventloop()
        self.lights = [wizlight(ip) for ip in self.ips]
        if discovery:
            self.lights.extend(
                force_sync(discovery.discover_lights, broadcast_space="192.168.1.255")
            )

    def send(self, config: dict):
        async def async_send(lights, builder):
            for light in lights:
                await light.turn_on(builder)

        force_sync(async_send, self.lights, PilotBuilder(**config))
