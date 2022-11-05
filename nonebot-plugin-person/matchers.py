from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot,GroupMessageEvent

import random

from .config import person_config

messages = [
    "{name}觉得{person}就是你要找的人",
    "{name}为你抽了一个人，是{person}",
    "{name}的神之力为你钦定了{person}",
    "让{name}想想，就{person}吧",
    "{name}随机抽取群里一名幸运观众，就这位吧，{person}"
]
nickname = list(person_config.nickname)[0]

get_person = on_command("随个人",priority=12)
@get_person.handle()
async def get_person_send(bot:Bot,event:GroupMessageEvent):
    group_id = event.group_id
    """
    获取群成员列表
    """
    group_member_list = await bot.get_group_member_list(group_id=group_id)
    member = random.choice(group_member_list)
    tosend = random.choice(messages) \
                .replace("{person}",f"{member['card'] if member['card'] else member['nickname']}（{member['user_id']}）") \
                .replace("{name}",nickname)
    await bot.send(event=event,message=tosend,at_sender=True)