from app.database.models import async_session
from app.database.models import User, Test
from sqlalchemy import select, update


async def set_user(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, name = name))
            session.add(Test(tg_id=tg_id,
                             test_past='🕗❌ Вы ещё не прошли все нужные темы!',
                             test_present='🕗❌ Вы ещё не прошли все нужные темы!',
                             test_future='🕗❌ Вы ещё не прошли все нужные темы!',
                             test_past_1=False,
                             test_past_2=False,
                             test_past_3=False,
                             test_past_4=False,
                             test_present_1=False,
                             test_present_2=False,
                             test_present_3=False,
                             test_present_4=False,
                             test_future_1=False,
                             test_future_2=False,
                             test_future_3=False,
                             test_future_4=False))
            await session.commit()
        else:
            user.name = name
            await session.commit()



async def get_profile(profile_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == profile_id))


async def get_test(profile_id):
    async with async_session() as session:
        return await session.scalar(select(Test).where(Test.tg_id == profile_id))


async def update_test_past(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        if user.test_past_1 + user.test_past_2 + user.test_past_3 + user.test_past_4 == 4:
            user.test_past = '🕗✅ Вы прошли все темы, связанные со временем Past! Теперь осталось только научиться летать в прошлое ;)'
        await session.commit()


async def update_test_present(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_present = '🕗✅ Вы прошли все темы, связанные со временем Present! Теперь только вы можете повелевать своим настоящим!'
        await session.commit()


async def update_test_future(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_future = '🕗✅ Вы прошли все темы, связанные со временем Future! Покупайте биткойн в 2013 и возвращайтесь назад в будущее :)'
        await session.commit()


async def update_test_past_1(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_past_1 = 1
        await session.commit()

async def update_test_past_2(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_past_2 = 1
        await session.commit()

async def update_test_past_3(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_past_3 = 1
        await session.commit()

async def update_test_past_4(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_past_4 = 1
        await session.commit()


async def update_test_present_1(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_present_1 = 1
        await session.commit()

async def update_test_present_2(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_present_2 = 1
        await session.commit()

async def update_test_present_3(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_present_3 = 1
        await session.commit()

async def update_test_present_4(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_present_4 = 1
        await session.commit()


async def update_test_future_1(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_future_1 = 1
        await session.commit()

async def update_test_future_2(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_future_2 = 1
        await session.commit()

async def update_test_future_3(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_future_3 = 1
        await session.commit()

async def update_test_future_4(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Test).where(Test.tg_id == tg_id))
        user.test_future_4 = 1
        await session.commit()