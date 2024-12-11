import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router
from app.q_past_1 import router1
from app.q_past_2 import router2
from app.q_past_3 import router3
from app.q_past_4 import router4
from app.q_present_1 import router5
from app.q_present_2 import router6
from app.q_present_3 import router7
from app.q_present_4 import router8
from app.q_future_1 import router9
from app.q_future_2 import router10
from app.q_future_3 import router11
from app.q_future_4 import router12
from app.database.models import async_main


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(router)
    dp.include_router(router1)
    dp.include_router(router2)
    dp.include_router(router3)
    dp.include_router(router4)
    dp.include_router(router5)
    dp.include_router(router6)
    dp.include_router(router7)
    dp.include_router(router8)
    dp.include_router(router9)
    dp.include_router(router10)
    dp.include_router(router11)
    dp.include_router(router12)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
