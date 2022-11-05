from .matchers import *
from nonebot.plugin import PluginMetadata

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="随个人",
    description="Nonebot2 简易插件随个人，随个群友当幸运观众🤪",
    usage="随个人XXX",
    extra={
        "version": __version__,
        "license": "MIT",
        "author": "jcjrobert <jcjrobbie@gmail.com>",
    },
)