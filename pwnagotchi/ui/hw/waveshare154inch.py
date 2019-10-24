import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Waveshare154inch(DisplayImpl):
    def __init__(self, config):
        super(Waveshare154inch, self).__init__(config, 'waveshare_1_54inch')
        self._display = None

    def layout(self):
        fonts.setup(10, 9, 10, 35)
        self._layout['width'] = 200
        self._layout['height'] = 200
        self._layout['face'] = (0, 54)
        self._layout['name'] = (5, 34)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (28, 0)
        self._layout['uptime'] = (199, 0)
        self._layout['line1'] = [0, 14, 264, 14]
        self._layout['line2'] = [0, 162, 264, 162]
        self._layout['friend_face'] = (0, 146)
        self._layout['friend_name'] = (40, 146)
        self._layout['shakes'] = (0, 163)
        self._layout['mode'] = (239, 163)
        self._layout['status'] = {
            'pos': (139, 34),
            'font': fonts.Medium,
            'max': 20
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare 1.54 inch display")
        from pwnagotchi.ui.hw.libs.waveshare.v154inch.epd1in54 import EPD
        self._display = EPD()
        self._display.init(EPD.lut_partial_update)
        self._display.Clear(0xFF)

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.display(buf)

    def clear(self):
        self._display.Clear(0xff)
