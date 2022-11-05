from pydantic import BaseModel, Extra
from typing import Set

from nonebot import get_driver

class Config(BaseModel, extra=Extra.ignore):
    nickname: Set[str] = {"Bot"}

person_config = Config.parse_obj(get_driver().config.dict())