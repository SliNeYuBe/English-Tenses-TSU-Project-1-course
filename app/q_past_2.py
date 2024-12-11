from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router2 = Router()


class Quiz(StatesGroup):
    QPaC1 = State()
    QPaC2 = State()
    QPaC3 = State()


@router2.message(F.text == 'Past Continuous')
async def past_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QPaC1)
    await state.update_data(correct_answers=0)
    question = qt.questions_past[3]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QPaC1)
async def past_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[3]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPaC2)
    question = qt.questions_past[4]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QPaC2)
async def past_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[4]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QPaC3)
    question = qt.questions_past[5]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QPaC3)
async def past_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_past[5]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Past Continues!",
            reply_markup=kb.main)
        await rq.update_test_past_2(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_past_1 + test.test_past_2 + test.test_past_3 + test.test_past_4 == 4:
            await rq.update_test_past(message.from_user.id)
            await message.answer('Вы полностью прошли время Past! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Past Continues!",
                             reply_markup=kb.main)
