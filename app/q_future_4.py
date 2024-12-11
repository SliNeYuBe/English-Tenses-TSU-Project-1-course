from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router12 = Router()


class Quiz(StatesGroup):
    QFPC1 = State()
    QFPC2 = State()
    QFPC3 = State()


@router12.message(F.text == 'Future Perfect Continuous')
async def future_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QFPC1)
    await state.update_data(correct_answers=0)
    question = qt.questions_future[9]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router12.message(Quiz.QFPC1)
async def future_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[9]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QFPC2)
    question = qt.questions_future[10]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router12.message(Quiz.QFPC2)
async def future_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[10]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QFPC3)
    question = qt.questions_future[11]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router12.message(Quiz.QFPC3)
async def future_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[11]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 3:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов и завершили тему Future Perfect Continuous!",
            reply_markup=kb.main)
        await rq.update_test_future_4(message.from_user.id)
        test = await rq.get_test(message.from_user.id)
        if test.test_future_1 + test.test_future_2 + test.test_future_3 + test.test_future_4 == 4 and '❌' in test.test_future:
            await rq.update_test_future(message.from_user.id)
            await message.answer('Вы полностью прошли время Future! Вы заслужили достижение! Перейдите в профиль, чтобы посмотреть его!')
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 3 вопросов! Ответьте на все вопросы правильно, чтобы завершить тему Future Perfect Continuous!",
                             reply_markup=kb.main)
