from nonebot import on_command
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    MessageSegment
)

import random
from datetime import datetime

from .config import person_config

messages = [
    "{name}觉得{person}就是你要找的人",
    "{name}为你抽了一个人，是{person}",
    "{name}的神之力为你钦定了{person}",
    "让{name}想想，就{person}吧",
    "{name}随机抽取群里一名幸运观众，就这位吧，{person}"
]
messages = messages + person_config.person_extra_messages \
    if not person_config.person_extra_messages_overwrite else person_config.person_extra_messages
nickname = person_config.nickname[0]

get_person = on_command("随个人",priority=12)
@get_person.handle()
async def get_person_send(bot:Bot,event:GroupMessageEvent):
    group_id = event.group_id
    group_member_list = await bot.get_group_member_list(group_id=group_id)
    if person_config.person_choose_last:
        group_member_list_last = [i for i in group_member_list if int(datetime.now().timestamp()) - i['last_sent_time'] < person_config.person_choose_last_time]
        if person_config.person_check_last:
            logger.info([(i['user_id'],i['nickname'],datetime.fromtimestamp(i['last_sent_time']).strftime("%Y-%m-%d %H:%M:%S")) for i in group_member_list])
            logger.info([(i['user_id'],i['nickname'],datetime.fromtimestamp(i['last_sent_time']).strftime("%Y-%m-%d %H:%M:%S")) for i in group_member_list_last])
        if group_member_list_last:
            group_member_list = group_member_list_last
        else:
            logger.error("当前群内没有指定时间内活跃的群友，默认抽取全部群友")
    member = random.choice(group_member_list)
    person = f"{member['card'] if member['card'] else member['nickname']}"
    if not person_config.person_at:
        person += f"（{member['user_id']}）"
    tosend = random.choice(messages) \
                .replace("{person}",person) \
                .replace("{name}",nickname)
    if person_config.person_show_avatar:
        avatar = f"http://q1.qlogo.cn/g?b=qq&nk={member['user_id']}&s=640"
        avatar = MessageSegment.image(file=avatar)
        tosend = "\n" + avatar + "\n" + tosend
        if person_config.person_at:
            tosend += MessageSegment.at(user_id=member['user_id'])
    await bot.send(event=event,message=tosend,at_sender=True)