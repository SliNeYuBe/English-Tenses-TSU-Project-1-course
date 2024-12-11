from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router3 = Router()


class Quiz(StatesGroup):
    QPaP1 = State()
    QPaP2 = State()
    QPaP3 = State()


@router3.message(F.text == 'Past Perfect')
async def past_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QPaP1)
    await state.update_data(correct_answers=0)
    question = qt.questions_past[6]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QPaP1)
async def past_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[6]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPaP2)
    question = qt.questions_past[7]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QPaP2)
async def past_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[7]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPaP3)
    question = qt.questions_past[8]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QPaP3)
async def past_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[8]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Past Perfect!",
            reply_markup=kb.main)
        await rq.update_test_past_3(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_past_1 + test.test_past_2 + test.test_past_3 + test.test_past_4 == 4:
            await rq.update_test_past(message.from_user.id)
            await message.answer('Вы полностью прошли время Past! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Past Perfect!",
                             reply_markup=kb.main)
