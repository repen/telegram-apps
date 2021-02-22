"""
Copyright (c) 2021 Plugin Andrey (9keepa@gmail.com)
Licensed under the MIT License
"""

from mebot.telegram import main as mebot, BaseCoordinator
import os

TOKEN = os.getenv("TOKEN", "")

class Command( BaseCoordinator ):

    def _start(self):
        """
        command /start
        """
        return "Привет!! Это твой Телеграм Бот. Готов тебе служить!"

    def _hello(self):
        "hello"
        first_name = self.tg_object["message"]["from"]["first_name"]
        return f"Hello `{first_name}`"

    def _echo(self):
        """
        command /echo
        """
        return f"{self.command}"


if __name__ == '__main__':

    mebot( token=TOKEN, coordinator = Command )