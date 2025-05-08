from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.database.request as rq
import app.keyboards as kb
from app.keyboards import test_choose, main_kb

router = Router()


tenses = ''

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.full_name)
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}!',
                         reply_markup=await main_kb(message.from_user.id))


@router.message(F.text == 'Профиль')
async def profile(message: Message):
    test = await rq.get_profile(message.from_user.id)
    if '✅' in test.achievements_past and '✅' in test.achievements_present and '✅' in test.achievements_future:
        await message.answer(
            f'🕗 Здравствуйте, Повелитель времени {message.from_user.full_name}! 🕗\n\nАчивки:\n\n{test.achievements_past[:2]} Past Tense: {test.achievements_past[3:]}'
            f'\n\n{test.achievements_present[:2]} Present Tense: {test.achievements_present[3:]}'
            f'\n\n{test.achievements_future[:2]} Future Tense: {test.achievements_future[3:]}')
    else:
        await message.answer(
            f'Здравствуйте, {message.from_user.full_name}!\n\nДостижения:\n\n{test.achievements_past[:2]} Past Tense: {test.achievements_past[3:]}'
            f'\n\n{test.achievements_present[:2]} Present Tense: {test.achievements_present[3:]}'
            f'\n\n{test.achievements_future[:2]} Future Tense: {test.achievements_future[3:]}')


@router.message(F.text == 'Обратная связь')
async def feedback(message: Message):
    await message.answer('Если возникли ошибки, вопросы или хотите предложить идею для доработки бота, обращайтесь ко мне в лс: @SliNeYuBe',
    reply_markup=await main_kb(message.from_user.id))


@router.message(F.text == 'Лекции')
async def lectures(message: Message):
    await message.answer('Выберите время, которое вас интересует: ', reply_markup=kb.time)


@router.callback_query(F.data == 'past')
async def category_past(callback: CallbackQuery):
    await callback.message.edit_text("Выберите одну из подгрупп времени Past: ", reply_markup=kb.category_past)


@router.callback_query(F.data == 'past_simple')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Past Simple'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild3734-3238-4538-b338-323135666661/-/format/webp/__2023-01-13__231709.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer('Все что нужно по Past Simple:\n\nhttps://www.native-english.ru/grammar/past-simple',
                                  reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'past_continuous')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Past Continuous'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6136-3835-4135-a231-363335653436/-/format/webp/__2023-01-13__232636.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Past Continuous:\n\nhttps://www.native-english.ru/grammar/past-continuous',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'past_perfect')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Past Perfect'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild3537-6135-4233-a361-663930313833/-/format/webp/__2023-01-13__233236.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Past Perfect:\n\nhttps://www.native-english.ru/grammar/past-perfect',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'past_perfect_continuous')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Past Perfect Continuous'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6565-3033-4261-b530-313332656337/-/format/webp/__2023-01-13__233823.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Past Perfect Continuous:\n\nhttps://www.native-english.ru/grammar/past-perfect-continuous',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'present')
async def category_past(callback: CallbackQuery):
    await callback.message.edit_text("Выберите одну из подгрупп времени Present: ", reply_markup=kb.category_present)


@router.callback_query(F.data == 'present_simple')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Present Simple'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild3235-3061-4564-a665-363537346661/-/format/webp/__2023-01-13__231353.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Present Simple:\n\nhttps://www.native-english.ru/grammar/present-simple',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'present_continuous')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Present Continuous'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild3962-3761-4565-b962-393737393438/-/format/webp/__2023-01-13__232253.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Present Continuous:\n\nhttps://www.native-english.ru/grammar/present-continuous',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'present_perfect')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Present Perfect'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6662-3537-4564-b934-373865633539/-/format/webp/__2023-01-13__233010.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Present Perfect:\n\nhttps://www.native-english.ru/grammar/present-perfect',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'present_perfect_continuous')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Present Perfect Continuous'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6538-3938-4238-b439-656133633661/-/format/webp/__2023-01-13__233719.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Present Perfect Continuous:\n\nhttps://www.native-english.ru/grammar/present-perfect-continuous',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'future')
async def category_past(callback: CallbackQuery):
    await callback.message.edit_text("Выберите одну из подгрупп времени Future: ", reply_markup=kb.category_future)


@router.callback_query(F.data == 'future_simple')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Future Simple'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild3763-3135-4730-b732-663437326638/-/format/webp/__2023-01-13__231938.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Future Simple:\n\nhttps://www.native-english.ru/grammar/future-simple',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'future_continuous')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Future Continuous'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6461-3335-4365-a563-366431343530/-/format/webp/__2023-01-13__232847.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Future Continuous:\n\nhttps://www.native-english.ru/grammar/future-continuous',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'future_perfect')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Future Perfect'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6232-3137-4534-b665-343837626361/-/format/webp/__2023-01-13__233433.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Future Perfect:\n\nhttps://www.native-english.ru/grammar/future-perfect',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'future_perfect_continuous')
async def category_past_simple(callback: CallbackQuery):
    global tenses
    tenses = 'Future Perfect Continuous'
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='https://optim.tildacdn.com/tild6230-3030-4631-b632-643964653561/-/format/webp/__2023-01-13__233948.png',
        caption='Как составить Positive/Negative/Question предложения'
    )
    await callback.message.answer(
        'Все что нужно по Future Perfect Continuous:\n\nhttps://www.native-english.ru/grammar/future-perfect-continuous',
        reply_markup=kb.main_or_test)


@router.callback_query(F.data == 'to_time')
async def category_time(callback: CallbackQuery):
    await callback.message.answer('Для начала теста нажмите кнопку с наименованием времени. Если передумали, можете вернуться обратно в меню',
                                  reply_markup= await test_choose(tenses))


@router.message(F.text == 'Назад')
async def to_return(message: Message):
    await message.answer('Вы вернулись в главное меню', reply_markup=await main_kb(message.from_user.id))


@router.message(F.text == 'Тесты')
async def choose_test(message: Message):
    await message.answer('Выберите один из тестов: ', reply_markup=kb.tests)


@router.message(F.text == 'Past')
async def choose_past(message: Message):
    await message.answer("Выберите одну из тем Past: ", reply_markup=kb.past)


@router.message(F.text == 'Present')
async def choose_past(message: Message):
    await message.answer("Выберите одну из тем Present: ", reply_markup=kb.present)


@router.message(F.text == 'Future')
async def choose_past(message: Message):
    await message.answer("Выберите одну из тем Future: ", reply_markup=kb.future)


@router.callback_query(F.data == 'back_time')
async def back_time(callback: CallbackQuery):
    await callback.message.answer(text='Вы вернулись обртано к временам', reply_markup=kb.time)
