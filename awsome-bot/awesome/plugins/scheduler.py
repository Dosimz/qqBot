from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='12', minute='12', second='12')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=1093427247,
                                 message=f'老八我已经吃完午饭了，大家午休下！不要忘记定闹钟起来学习哦')
    except CQHttpError:
        pass