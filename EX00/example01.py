"""
Copyright (c) 2021 Plugin Andrey (9keepa@gmail.com)
Licensed under the MIT License
"""

from mebot.telegram import main as mebot, BaseCoordinator
import os, time
from itertools import count

TOKEN = os.getenv("TOKEN", "")

class Command( BaseCoordinator ):

    def _play(self):

        if self.storage.get("work"):
            return "Извините метод уже запущен!!"

        self.storage["work"] = True
        for c in count(start=1):

            if not self.storage["work"]:
                break

            if c == 10:
                break

            self.send_message(f"{c}. Spam")
            time.sleep(1)

        return "end work"

    def _stop(self):
        self.storage["work"] = False

    def _stop3(self):
        time.sleep(3)
        self.storage["work"] = False





if __name__ == '__main__':

    mebot( token=TOKEN, coordinator = Command )