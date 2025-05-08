from aiogram import F, Router
from aiogram.types import Message

import app.database.request as rq
from app.keyboards import main_kb

router_admin = Router()

@router_admin.message(F.text == "Админ панель")
async def admin(message: Message):
    users = await rq.get_all_profile()
    answer = "Все зарегистрированные пользователи: \n\n"
    for user in users:
        answer += (f"Телеграм ID: {user.tg_id}\nИмя: {user.name}\nКоличество решенных разделов: {user.complete_tests}/3\n\n~~~~~~~~~~~~~~~~\n\n")
    await message.answer(answer, reply_markup=await main_kb(message.from_user.id))
