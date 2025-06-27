from nonebot import require, get_plugin_config
from nonebot.plugin import PluginMetadata
from clovers.config import Config as CloversConfig
from .config import Config

require("nonebot_plugin_clovers")
from nonebot_plugin_clovers import client as nbcc, __plugin_meta__ as nbcc_plugin_meta


__plugin_meta__ = PluginMetadata(
    name="AI群聊机器人",
    description="AI群聊机器人",
    usage="@BOT 聊天内容",
    type="application",
    config=Config,
    homepage="https://github.com/KarisAya/nonebot_plugin_groups_aichat",
    supported_adapters=nbcc_plugin_meta.supported_adapters,
)

import_name = "clovers_aichat"

CloversConfig.environ()[import_name] = {k.lower().lstrip("groups_aichat_"): v for k, v in get_plugin_config(Config).model_dump().items()}

nbcc.load_plugin(import_name)
