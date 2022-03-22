from capture.CapturerFactory import CapturerFactory
from common.utils import yaml_load
from orchestrators import ExecuteOrchestrator, CaptureOrchestrator
from smartLight.ControllerFactory import ControllerFactory
import queue
import argparse


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    return parser.parse_args()


def main(cfg):
    light = cfg.get("light", {})

    print("Creating Queue")
    runtime_queue = queue.LifoQueue(light.get("queue_size", 10))
    if light.get("type") == "wiz":
        print("Connecting to Wiz")
        controller = ControllerFactory.get_wiz_controller(
            light.get("lights", []), light.get("discovery", False)
        )
    else:
        print("This app do not support other controllers")
        return

    capture = CapturerFactory.get_win_capturer()
    capturer = CaptureOrchestrator(runtime_queue, capture)
    executor = ExecuteOrchestrator(runtime_queue, controller, cfg.get("image_compression", 50))

    print("Starting Image Capturer")
    capturer.start()
    print("Starting Executor")
    executor.start()
    while True:
        pass


if __name__ == "__main__":
    args = parseArgs()
    main(yaml_load(args.config))
