import time
import vk_api
import logging
from vk_api.utils import get_random_id

import bot.command
import localization
from bot.command import Command
import setting
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

logging.basicConfig(filename='app.log',
                    filemode='a',
                    level=logging.INFO)

while True:
    try:
        vk_session = vk_api.VkApi(token=setting.TOKEN)
        longpool = VkBotLongPoll(vk_session, setting.BOT_ID)
        vk = vk_session.get_api()

        for event in longpool.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object['message']['text']
                user_id = event.object['message']['from_id']
                id = event.object['message']['id']
                peer = event.object['message']['peer_id']
                if user_id > 0:
                    if "[public213954453|@cherry_bp_bot] " in text.lower():
                        text = text[28:]
                    elif 'action' in event.object['message'] and event.object['message']['action'][
                        'type'] == 'chat_invite_user' and \
                            event.object['message']['action']['member_id'] == -213954453:
                        vk.messages.send(random_id=get_random_id(), peer_id=peer,
                                         message=localization.INVITE_TO_GROUP)
                    bot.command.Command(user_id, peer, id, text)

    except Exception as ex:
        end_log = str(Exception)
        logging.exception(end_log)
        time.sleep(5)
