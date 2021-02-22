"""
Copyright (c) 2021 Plugin Andrey (9keepa@gmail.com)
Licensed under the MIT License
"""

from mebot.telegram import main as mebot, BaseCoordinator
import os

TOKEN = os.getenv("TOKEN", "")

class Command(BaseCoordinator):
    """
    Атрибуты класса:
    'tg_object' --  данные от телеграма
    'chat_id' -- чат id
    'api_url' -- урл с токеном
    'command' -- команда которая была вызвана
    'storage' -- словарь для хранения различных данных для каждого клиента

    Доступ осуществляется через self.tg_object, self.chat_id и т.д.
    """

    def _start(self):
        """
        command /start
        """
        return "Привет!! Это твой Телеграм Бот. Готов тебе служить!"

    def _echo(self):
        """
        command /echo
        """
        return f"{self.command}"


if __name__ == '__main__':
    mebot(token=TOKEN, coordinator=Command)