from pydantic import BaseModel, Extra
from typing import Set, List

from nonebot import get_driver

class Config(BaseModel, extra=Extra.ignore):
    nickname: Set[str] = {"Bot"}
    person_show_avatar: bool = True
    person_extra_messages: List[str] = []
    person_extra_messages_overwrite: bool = False
    person_at: bool = False

person_config = Config.parse_obj(get_driver().config.dict())