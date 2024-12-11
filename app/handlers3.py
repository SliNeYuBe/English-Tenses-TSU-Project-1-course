from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router3 = Router()


class Quiz(StatesGroup):
    QF1 = State()
    QF2 = State()
    QF3 = State()
    QF4 = State()
    QF5 = State()
    QF6 = State()
    QF7 = State()
    QF8 = State()
    QF9 = State()
    QF10 = State()
    QF11 = State()
    QF12 = State()


@router3.message(F.text == 'Future')
async def past_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QF1)
    await state.update_data(correct_answers=0)
    question = qt.questions_future[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF1)
async def past_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[0]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF2)
    question = qt.questions_future[1]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF2)
async def past_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[1]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF3)
    question = qt.questions_future[2]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF3)
async def past_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[2]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF4)
    question = qt.questions_future[3]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF4)
async def past_answer_5(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[3]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF5)
    question = qt.questions_future[4]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF5)
async def past_answer_6(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[4]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF6)
    question = qt.questions_future[5]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF6)
async def past_answer_7(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[5]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF7)
    question = qt.questions_future[6]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF7)
async def past_answer_8(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[6]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF8)
    question = qt.questions_future[7]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF8)
async def past_answer_9(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[7]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF9)
    question = qt.questions_future[8]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF9)
async def past_answer_10(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[8]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF10)
    question = qt.questions_future[9]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF10)
async def past_answer_11(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[9]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF11)
    question = qt.questions_future[10]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF11)
async def past_answer_12(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[10]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QF12)
    question = qt.questions_future[11]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router3.message(Quiz.QF12)
async def past_answer_final(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_future[11]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 12:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 12 вопросов! В вашем профиле появилось достижение за прохождение теста на время Future!",
            reply_markup=kb.main)
        await rq.update_test_future(message.from_user.id)
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 12 вопросов!",
                             reply_markup=kb.main)
