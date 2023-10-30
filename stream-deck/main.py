import threading
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from pathlib import Path
from PIL import Image

# IMAGE PATHS

ASSET_FILE_PATH = Path(__file__).parent.parent / "assets"
KEY_MAPS = {}
IMG_MAPS = {}

def key_change_callback(deck, key, state):

    print(f"Deck {deck.id()} Key {key} = {"down" if state else "up"}", flush=True)


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    for index, deck in enumerate(streamdecks):
        deck.open()

        # Register callback function for when a key state changes.
        deck.set_key_callback(key_change_callback)

        filename = "test.jpg"
        image = Image.open(filename)
        image = PILHelper.to_native_format(deck, image)
        deck.set_key_image(0, image)

        
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                pass

