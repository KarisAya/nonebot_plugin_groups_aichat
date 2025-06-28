from nonebot import require, get_plugin_config
from nonebot.plugin import PluginMetadata
from clovers.config import Config as CloversConfig
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="AI群聊机器人",
    description="AI群聊机器人",
    usage="@BOT 聊天内容",
    type="application",
    config=Config,
    homepage="https://github.com/KarisAya/nonebot_plugin_groups_aichat",
    supported_adapters=None,
)

IMPORT_NAME = "clovers_aichat"
PREFIX_LENGTH = len("groups_aichat_")
CloversConfig.environ()[IMPORT_NAME] = {k[PREFIX_LENGTH:].lower(): v for k, v in get_plugin_config(Config).model_dump().items()}
require("nonebot_plugin_clovers").client.load_plugin(IMPORT_NAME)
