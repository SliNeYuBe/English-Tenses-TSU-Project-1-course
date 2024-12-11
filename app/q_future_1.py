from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router9 = Router()


class Quiz(StatesGroup):
    QFS1 = State()
    QFS2 = State()
    QFS3 = State()


@router9.message(F.text == 'Future Simple')
async def future_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QFS1)
    await state.update_data(correct_answers=0)
    question = qt.questions_future[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router9.message(Quiz.QFS1)
async def future_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[0]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QFS2)
    question = qt.questions_future[1]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router9.message(Quiz.QFS2)
async def future_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[1]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QFS3)
    question = qt.questions_future[2]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router9.message(Quiz.QFS3)
async def future_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[2]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Future Simple!",
            reply_markup=kb.main)
        await rq.update_test_future_1(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_future_1 + test.test_future_2 + test.test_future_3 + test.test_future_4 == 4 and '❌' in test.test_future:
            await rq.update_test_future(message.from_user.id)
            await message.answer('Вы полностью прошли время Future! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Future Simple!",
                             reply_markup=kb.main)
