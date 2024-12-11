from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router8 = Router()


class Quiz(StatesGroup):
    QPrPC1 = State()
    QPrPC2 = State()
    QPrPC3 = State()


@router8.message(F.text == 'Present Perfect Continuous')
async def present_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QPrPC1)
    await state.update_data(correct_answers=0)
    question = qt.questions_present[9]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router8.message(Quiz.QPrPC1)
async def present_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[9]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPrPC2)
    question = qt.questions_present[10]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router8.message(Quiz.QPrPC2)
async def present_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[10]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPrPC3)
    question = qt.questions_present[11]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router8.message(Quiz.QPrPC3)
async def present_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[11]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Present Perfect Continuous!",
            reply_markup=kb.main)
        await rq.update_test_present_4(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_present_1 + test.test_present_2 + test.test_present_3 + test.test_present_4 == 4 and '❌' in test.test_present:
            await rq.update_test_present(message.from_user.id)
            await message.answer('Вы полностью прошли время Present! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Present Perfect Continuous!",
                             reply_markup=kb.main)
