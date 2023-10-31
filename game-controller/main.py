from evdev import InputDevice, categorize
from pathlib import Path

CONTROLLER_FILE_PATH = Path('/dev/input/event19')

controller = InputDevice(CONTROLLER_FILE_PATH)

for event in controller.read_loop():
    print(categorize(event))
