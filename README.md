<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-Groups-AIchat

AI 群聊机器人群聊

[![python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![license](https://img.shields.io/github/license/KarisAya/nonebot_plugin_groups_aichat.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot_plugin_groups_aichat.svg)](https://pypi.python.org/pypi/nonebot_plugin_groups_aichat)
[![pypi download](https://img.shields.io/pypi/dm/nonebot_plugin_groups_aichat)](https://pypi.python.org/pypi/nonebot_plugin_groups_aichat)
<br />

[![机器人 bug 研究中心](https://img.shields.io/badge/QQ%E7%BE%A4-744751179-maroon?)](https://qm.qq.com/q/3vpD9Ypb0c)

</div>

# 安装

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot_plugin_groups_aichat
```

</details>

<details>
<summary>使用包管理工具</summary>

使用 poetry/pip 等包管理工具在当前目录安装本插件

之后打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_groups_aichat"
]
```

</details>

</div>

# 配置

具体配置方法请参考 [clovers-aichat](https://github.com/clovers-project/clovers-aichat)

```env
GROUPS_AICHAT_TIMEOUT = 600
GROUPS_AICHAT_MEMORY = 20
GROUPS_AICHAT_STYLE_PROMPT = '你的名字是枫枫，你可以自由回答问题。'
GROUPS_AICHAT_CONFIG_LIST = '
[
	{
		"key": "hunyuan",
		"model": "hunyuan-lite",
		"url": "https://hunyuan.tencentcloudapi.com",
		"secret_id": "",
		"secret_key": ""
	}
]
'
```
