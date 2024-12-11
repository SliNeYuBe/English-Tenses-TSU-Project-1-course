from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router2 = Router()


class Quiz(StatesGroup):
    QP1 = State()
    QP2 = State()
    QP3 = State()
    QP4 = State()
    QP5 = State()
    QP6 = State()
    QP7 = State()
    QP8 = State()
    QP9 = State()
    QP10 = State()
    QP11 = State()
    QP12 = State()


@router2.message(F.text == 'Present')
async def past_answer_1(message: Message, state: FSMContext):
    await state.set_state(Quiz.QP1)
    await state.update_data(correct_answers=0)
    question = qt.questions_present[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP1)
async def past_answer_2(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[0]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP2)
    question = qt.questions_present[1]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP2)
async def past_answer_3(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[1]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP3)
    question = qt.questions_present[2]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP3)
async def past_answer_4(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[2]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP4)
    question = qt.questions_present[3]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP4)
async def past_answer_5(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[3]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP5)
    question = qt.questions_present[4]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP5)
async def past_answer_6(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[4]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP6)
    question = qt.questions_present[5]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP6)
async def past_answer_7(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[5]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP7)
    question = qt.questions_present[6]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP7)
async def past_answer_8(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[6]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP8)
    question = qt.questions_present[7]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP8)
async def past_answer_9(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[7]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP9)
    question = qt.questions_present[8]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP9)
async def past_answer_10(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[8]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP10)
    question = qt.questions_present[9]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP10)
async def past_answer_11(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[9]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP11)
    question = qt.questions_present[10]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP11)
async def past_answer_12(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[10]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.set_state(Quiz.QP12)
    question = qt.questions_present[11]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router2.message(Quiz.QP12)
async def past_answer_final(message: Message, state: FSMContext):
    answer = message.text
    correct_answer = qt.questions_present[11]['correct']

    data = await state.get_data()
    correct_answers = data.get('correct_answers', 0)
    if answer == correct_answer:
        correct_answers += 1
        await state.update_data(correct_answers=correct_answers)

    await state.clear()
    if correct_answers == 12:
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из 12 вопросов! В вашем профиле появилось достижение за прохождение теста на время Present!",
            reply_markup=kb.main)
        await rq.update_test_present(message.from_user.id)
    else:
        await message.answer(f"Тест завершен! Вы ответили правильно на {correct_answers} из 12 вопросов!",
                             reply_markup=kb.main)
