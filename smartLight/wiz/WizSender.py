from common import force_sync
from pywizlight import wizlight, PilotBuilder, discovery
from common.utils import get_fps, get_or_create_eventloop, get_time
from ..interface.Sender import Sender
import socket
import json


class WizSender(Sender):
    def __init__(self, ips=[], discovery=False) -> None:
        self.ips = ips
        self.discovery = discovery
        self.eventLoop = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def configure(self):
        self.eventLoop = get_or_create_eventloop()
        self.lights = [wizlight(ip) for ip in self.ips]
        if discovery:
            self.lights.extend(
                self.eventLoop.run_until_complete(
                    discovery.discover_lights(broadcast_space="192.168.1.255")
                )
            )

    def _get_wiz_json(self, data):
        return json.dumps(data, separators=(",", ":"))

    def _send_udp_message(self, message, ip, port):
        data = message.encode("utf-8")
        self.sock.sendto(data, (ip, port))

    def send(self, config: dict):
        for light in self.lights:
            msg = PilotBuilder(**config).set_pilot_message()
            wizmsg = self._get_wiz_json(msg)
            self._send_udp_message(wizmsg, light.ip, light.port)
