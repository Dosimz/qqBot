from nonebot import on_command, CommandSession
import datetime

@on_command('countdown', aliases=('考研倒计时','离考研还有多少天','还有多少天考研'))
async def countdown(session: CommandSession):
    countdown_report = await get_count_day()

    await session.send(countdown_report)

async def get_count_day() -> str:
    final_day = datetime.datetime(2020,12,22)
    nowadays = datetime.datetime.now()
    interval = final_day - nowadays
    # print(interval.days - 2)
    return f'离考研还有{interval.days - 2}天'