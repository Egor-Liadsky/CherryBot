import logging
import localization
import vk_api
from vk_api.utils import get_random_id

import setting

logging.basicConfig(filename='command.log',
                    filemode='a',
                    level=logging.INFO
                    )

vk_session = vk_api.VkApi(token=setting.TOKEN)
vk = vk_session.get_api()


class Command:
    def __init__(self, user_id: int, peer: int, chat_id: int, text: str):
        super(Command, self).__init__()

        command_dict = {"help": {"synonym": ['помощь', 'help'], 'func': self.help_msg}}

        self.peer = peer
        self.user_id = user_id
        self.chat_id = chat_id
        self.text = text.lower()

        for command in command_dict:
            for synonym_command in command_dict[command]['synonym']:
                synonym_command_len = len(synonym_command)
                if " " in synonym_command:
                    if synonym_command == self.text[:synonym_command_len]:
                        cmd = self.text[:synonym_command_len]
                        self.args = self.text.split(cmd)
                        self.command = cmd
                        del self.args[0]
                        command_dict[command]['func']()
                        self.break_block = True
                        break
                else:
                    if synonym_command == self.text:
                        cmd = self.text
                        self.args = self.text.split(cmd)
                        self.command = cmd
                        del self.args[0]
                        command_dict[command]['func']()
                        self.break_block = True
                        break
            if self.break_block:
                break

    # Помощь по командам
    def help_msg(self):
        return self.send_message(message=localization.HELP_MSG)

    # Метод для отправки сообщения пользователю
    def send_message(self, message):
        return vk.messages.send(random_id=get_random_id(), peer_id=self.peer, message=message)
