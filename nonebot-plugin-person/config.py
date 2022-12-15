from pydantic import BaseModel, Extra, validator
from typing import List

from nonebot import get_driver

class Config(BaseModel, extra=Extra.ignore):
    nickname: List[str] = ["Bot"]
    person_show_avatar: bool = True
    person_extra_messages: List[str] = []
    person_extra_messages_overwrite: bool = False
    person_at: bool = False
    person_choose_last: bool = False
    person_choose_last_time: int = 2592000
    person_check_last: bool = False

    @validator("nickname")
    @classmethod
    def check_nickname(cls, nickname):
        if not nickname:
            nickname = ["Bot"]
        return nickname

person_config = Config.parse_obj(get_driver().config.dict())