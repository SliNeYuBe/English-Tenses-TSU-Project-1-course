from sqlalchemy import select

from app.database.models import User, Admin, TestPast, TestPresent, TestFuture
from app.database.models import async_session


async def set_user(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id,
                             name = name,
                             achievements_past='🕗❌ Вы ещё не прошли все нужные темы!',
                             achievements_present='🕗❌ Вы ещё не прошли все нужные темы!',
                             achievements_future='🕗❌ Вы ещё не прошли все нужные темы!',
                             complete_tests=0))

            session.add(Admin(tg_id=None))

            session.add(TestPast(tg_id=tg_id,
                             test_past_1=False,
                             test_past_2=False,
                             test_past_3=False,
                             test_past_4=False))

            session.add(TestPresent(tg_id=tg_id,
                             test_present_1=False,
                             test_present_2=False,
                             test_present_3=False,
                             test_present_4=False))

            session.add(TestFuture(tg_id=tg_id,
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


async def get_all_profile():
    async with async_session() as session:
        result = await session.scalars(select(User))
        return result.all()


async def get_admin(profile_id):
    async with async_session() as session:
        return await session.scalar(select(Admin).where(Admin.tg_id == profile_id))


BD_SETS = {
    "Past Simple": "test_past_1",
    "Past Continuous": "test_past_2",
    "Past Perfect": "test_past_3",
    "Past Perfect Continuous": "test_past_4",
    "Present Simple": "test_present_1",
    "Present Continuous": "test_present_2",
    "Present Perfect": "test_present_3",
    "Present Perfect Continuous": "test_present_4",
    "Future Simple": "test_future_1",
    "Future Continuous": "test_future_2",
    "Future Perfect": "test_future_3",
    "Future Perfect Continuous": "test_future_4"
}


async def update_big_test(tg_id, field_test):
    async with async_session() as session:
        achievement_test = ""
        sum_test = 0

        if "Past" in field_test:
            field_test = "achievements_past"
            model = TestPast
            test = await session.scalar(select(model).where(model.tg_id == tg_id))
            achievement_test = '🕗✅ Вы прошли все темы, связанные со временем Past! Теперь осталось только научиться летать в прошлое ;)'
            sum_test = test.test_past_1 + test.test_past_2 + test.test_past_3 + test.test_past_4

        elif "Present" in field_test:
            field_test = "achievements_present"
            model = TestPresent
            test = await session.scalar(select(model).where(model.tg_id == tg_id))
            achievement_test = '🕗✅ Вы прошли все темы, связанные со временем Present! Теперь только вы можете повелевать своим настоящим!'
            sum_test = test.test_present_1 + test.test_present_2 + test.test_present_3 + test.test_present_4

        elif "Future" in field_test:
            field_test = "achievements_future"
            model = TestFuture
            test = await session.scalar(select(model).where(model.tg_id == tg_id))
            achievement_test = '🕗✅ Вы прошли все темы, связанные со временем Future! Покупайте биткойн в 2013 и возвращайтесь назад в будущее :)'
            sum_test = test.test_future_1 + test.test_future_2 + test.test_future_3 + test.test_future_4

        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if sum_test == 4 and getattr(user, field_test) == '🕗❌ Вы ещё не прошли все нужные темы!':
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            setattr(user, field_test, achievement_test)
            user.complete_tests += 1
            await session.commit()
            return True


async def update_small_test(tg_id, field_name, value = 1):
    async with async_session() as session:
        if "Past" in field_name:
            model = TestPast

        elif "Present" in field_name:
            model = TestPresent

        elif "Future" in field_name:
            model = TestFuture
        user = await session.scalar(select(model).where(model.tg_id == tg_id))
        setattr(user, BD_SETS[field_name], value)
        await session.commit()