from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router1 = Router()


class Quiz(StatesGroup):
    QPaS1 = State()
    QPaS2 = State()
    QPaS3 = State()


@router1.message(F.text == 'Past Simple')
async def past_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QPaS1)
    await state.update_data(correct_answers=0)
    question = qt.questions_past[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router1.message(Quiz.QPaS1)
async def past_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[0]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPaS2)
    question = qt.questions_past[1]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router1.message(Quiz.QPaS2)
async def past_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[1]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPaS3)
    question = qt.questions_past[2]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router1.message(Quiz.QPaS3)
async def past_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[2]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Past Simple!",
            reply_markup=kb.main)
        await rq.update_test_past_1(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_past_1 + test.test_past_2 + test.test_past_3 + test.test_past_4 == 4 and '❌' in test.test_past:
            await rq.update_test_past(message.from_user.id)
            await message.answer('Вы полностью прошли время Past! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Past Simple!",
                             reply_markup=kb.main)
