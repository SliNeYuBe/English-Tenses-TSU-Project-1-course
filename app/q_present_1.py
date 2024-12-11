from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router5 = Router()


class Quiz(StatesGroup):
    QPrS1 = State()
    QPrS2 = State()
    QPrS3 = State()


@router5.message(F.text == 'Present Simple')
async def present_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QPrS1)
    await state.update_data(correct_answers=0)
    question = qt.questions_present[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router5.message(Quiz.QPrS1)
async def present_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[0]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPrS2)
    question = qt.questions_present[1]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router5.message(Quiz.QPrS2)
async def present_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[1]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPrS3)
    question = qt.questions_present[2]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router5.message(Quiz.QPrS3)
async def present_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[2]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Present Simple!",
            reply_markup=kb.main)
        await rq.update_test_present_1(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_present_1 + test.test_present_2 + test.test_present_3 + test.test_present_4 == 4 and '❌' in test.test_present:
            await rq.update_test_present(message.from_user.id)
            await message.answer('Вы полностью прошли время Present! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Present Simple!",
                             reply_markup=kb.main)
