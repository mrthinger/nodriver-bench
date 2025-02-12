"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""

import logging


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        logging.info("We've seen %d flows" % self.num)
        logging.info(flow)
        with open("requests.log", "a") as f:
            f.write(f"Flow #{self.num}: {flow}\n")


addons = [Counter()]
