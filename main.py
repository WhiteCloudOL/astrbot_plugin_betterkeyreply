from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult  
from astrbot.api.message_components import *
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register(
    "betterkeyreply",
    "WhiteCloudOL",
    "更好的关键词回复插件。",
    "1.0.0",
    "https://github.com/WhiteCloudOL/astrbot_plugin_betterkeyreply",
)
class Betterkeyreply(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册指令的装饰器。指令名为 bkrhelp。注册成功后，发送 `/bkrhelp` 就会触发这个指令。
    @filter.command("bkrhelp",alias={"关键词回复帮助", "关键词回复说明", "bkrh", "bkr"})
    async def helloworld(self, event: AstrMessageEvent):
        """获取插件帮助信息。""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息


    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
