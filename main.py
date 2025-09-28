# current_time.py
from datetime import datetime
from pkg.plugin.context import register, handler, BasePlugin, EventContext
from pkg.plugin.events import *


@register(
    name="CurrentTime",
    description="发送“当前时间”返回具体时间与所处时段",
    version="0.3",
    author="RockChinQ"
)
class CurrentTimePlugin(BasePlugin):

    def __init__(self, host):
        super().__init__(host)

    # 工具：返回“时间+时段”字符串
    def _time_info(self) -> str:
        now = datetime.now()
        h = now.hour
        if 5 <= h < 12:
            period = "上午"
        elif 12 <= h < 18:
            period = "下午"
        elif 18 <= h < 24:
            period = "晚上"
        else:
            period = "凌晨"
        return f"当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}，现在是{period}。"

    # 私聊
    @handler(PersonNormalMessageReceived)
    async def on_person_msg(self, ctx: EventContext):
        if ctx.event.text_message.strip() == "当前时间":
            ctx.add_return("reply", [self._time_info()])
            ctx.prevent_default()

    # 群聊
    @handler(GroupNormalMessageReceived)
    async def on_group_msg(self, ctx: EventContext):
        if ctx.event.text_message.strip() == "当前时间":
            ctx.add_return("reply", [self._time_info()])
            ctx.prevent_default()
