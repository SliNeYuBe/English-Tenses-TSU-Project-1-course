from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from pyexpat.errors import messages

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq
from app.keyboards import test_choose

router = Router()

'''
class Quiz(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()
    Q11 = State()
    Q12 = State()
'''


tenses = ''

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.full_name)
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}!',
                         reply_markup=kb.main)


@router.message(F.text == 'Профиль')
async def profile(message: Message):
    test = await rq.get_test(message.from_user.id)
    test_past = test.test_past_1 + test.test_past_2 + test.test_past_3 + test.test_past_4
    test_present = test.test_present_1 + test.test_present_2 + test.test_present_3 + test.test_present_4
    test_future = test.test_future_1 + test.test_future_2 + test.test_future_3 + test.test_future_4
    if test_past == test_present == test_future == 4:
        await message.answer(
            f'🕗 Здравствуйте, Повелитель времени {message.from_user.full_name}! 🕗\n\nАчивки:\n\n{test.test_past[:2]} Past Test: {test.test_past[3:]}'
            f'\n\n{test.test_present[:2]} Present Test: {test.test_present[3:]}'
            f'\n\n{test.test_future[:2]} Future Test: {test.test_future[3:]}')
    else:
        await message.answer(
            f'Здравствуйте, {message.from_user.full_name}!\n\nДостижения:\n\n{test.test_past[:2]} Past Test: {test.test_past[3:]}'
            f'\n\n{test.test_present[:2]} Present Test: {test.test_present[3:]}'
            f'\n\n{test.test_future[:2]} Future Test: {test.test_future[3:]}')


@router.message(F.text == 'Обратная связь')
async def feedback(message: Message):
    await message.answer('Если возникли ошибки, вопросы или хотите предложить идею для доработки бота, обращайтесь ко мне в лс: @SliNeYuBe',
    reply_markup=kb.main)


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
    await message.answer('Вы вернулись в главное меню', reply_markup=kb.main)


@router.message(F.text == 'Тесты')
async def choose_test(message: Message):
    await message.answer('Выберите один из тестов: ', reply_markup=kb.tests)


@router.message(F.text == 'Past')
async def choose_past(message: Message):
    await message.answer("Выберите одну из тем Past: ", reply_markup=kb.past)


@router.message(F.text == 'Present')
async def choose_past(message: Message):
    await message.answer("Выберите одну из тем Past: ", reply_markup=kb.present)


@router.message(F.text == 'Future')
async def choose_past(message: Message):
    await message.answer("Выберите одну из тем Past: ", reply_markup=kb.future)
'''
@router.message(F.text == 'Past')
async def past_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.Q1)
    await state.update_data(correct_answers=0)
    question = qt.questions_past[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q1)
async def past_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[0]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q2)
    question = qt.questions_past[1]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q2)
async def past_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[1]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q3)
    question = qt.questions_past[2]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q3)
async def past_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[2]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q4)
    question = qt.questions_past[3]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q4)
async def past_answer_5(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[3]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q5)
    question = qt.questions_past[4]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q5)
async def past_answer_6(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[4]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q6)
    question = qt.questions_past[5]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q6)
async def past_answer_7(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[5]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q7)
    question = qt.questions_past[6]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q7)
async def past_answer_8(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[6]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q8)
    question = qt.questions_past[7]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q8)
async def past_answer_9(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[7]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q9)
    question = qt.questions_past[8]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q9)
async def past_answer_10(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[8]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q10)
    question = qt.questions_past[9]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q10)
async def past_answer_11(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[9]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q11)
    question = qt.questions_past[10]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q11)
async def past_answer_12(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[10]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.Q12)
    question = qt.questions_past[11]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router.message(Quiz.Q12)
async def past_answer_final(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[11]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 12:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 12 вопросов! В вашем профиле появилось достижение за прохождение теста на время Past!",
            reply_markup=kb.main)
        await rq.update_test_past(message.from_user.id)
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 12 вопросов!",
                             reply_markup=kb.main)
'''

@router.callback_query(F.data == 'back_time')
async def back_time(callback: CallbackQuery):
    await callback.message.answer(text='Вы вернулись обртано к временам', reply_markup=kb.time)
