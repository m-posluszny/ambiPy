from capture.CapturerFactory import CapturerFactory
from common.utils import yaml_load
from orchestrators import SenderOrchestrator, ImageOrchestrator
from smartLight.ControllerFactory import ControllerFactory
from structures import CappedQueue
import argparse


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    return parser.parse_args()


def main(cfg):
    light = cfg.get("light", {})
    print("Creating Queue")
    colorQueue = CappedQueue(maxsize=light.get("queue_size", 100))

    if light.get("type") == "wiz":
        print("Connecting to Wiz")
        controller = ControllerFactory.get_wiz_controller(
            light.get("lights", []), light.get("discovery", False)
        )
    else:
        print("This app do not support other controllers")
        return

    capture = CapturerFactory.get_win_capturer()
    imager = ImageOrchestrator(colorQueue, capture, cfg.get("image_compression", 50))
    sender = SenderOrchestrator(colorQueue, controller)

    print("Starting Image Capturer & Parser")
    imager.start()
    print("Starting Sender")
    sender.start()
    while True:
        pass


if __name__ == "__main__":
    args = parseArgs()
    main(yaml_load(args.config))
