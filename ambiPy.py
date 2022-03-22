from capture.CapturerFactory import CapturerFactory
from orchestrators import ExecuteOrchestrator, CaptureOrchestrator
import queue

from smartLight.ControllerFactory import ControllerFactory


def main():
    print("Creating Queue")
    runtime_queue = queue.Queue(10)
    controller = ControllerFactory.get_wiz_controller()
    capture = CapturerFactory.get_win_capturer()

    capturer = CaptureOrchestrator(runtime_queue, capture)
    executor = ExecuteOrchestrator(runtime_queue, controller, 50)

    print("Starting Image Capturer")
    capturer.start()
    print("Starting Executor")
    executor.start()
    while True:
        pass


if __name__ == "__main__":
    main()
