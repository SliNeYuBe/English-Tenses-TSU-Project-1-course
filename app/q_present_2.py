from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router6 = Router()


class Quiz(StatesGroup):
    QPrC1 = State()
    QPrC2 = State()
    QPrC3 = State()


@router6.message(F.text == 'Present Continuous')
async def present_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QPrC1)
    await state.update_data(correct_answers=0)
    question = qt.questions_present[3]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router6.message(Quiz.QPrC1)
async def present_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[3]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPrC2)
    question = qt.questions_present[4]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router6.message(Quiz.QPrC2)
async def present_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[4]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPrC3)
    question = qt.questions_present[5]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router6.message(Quiz.QPrC3)
async def present_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[5]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Present Continuous!",
            reply_markup=kb.main)
        await rq.update_test_present_2(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_present_1 + test.test_present_2 + test.test_present_3 + test.test_present_4 == 4 and '❌' in test.test_present:
            await rq.update_test_present(message.from_user.id)
            await message.answer('Вы полностью прошли время Present! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Present Continuous!",
                             reply_markup=kb.main)
