from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.keyboards import main_kb

import app.questions as qt
import app.keyboards as kb
import app.database.request as rq

router0 = Router()

QUESTION_SETS = {
    "Past Simple": qt.questions_past_simple,
    "Past Continuous": qt.questions_past_continuous,
    "Past Perfect": qt.questions_past_perfect,
    "Past Perfect Continuous": qt.questions_past_perfect_continuous,
    "Present Simple": qt.questions_present_simple,
    "Present Continuous": qt.questions_present_continuous,
    "Present Perfect": qt.questions_present_perfect,
    "Present Perfect Continuous": qt.questions_present_perfect_continuous,
    "Future Simple": qt.questions_future_simple,
    "Future Continuous": qt.questions_future_continuous,
    "Future Perfect": qt.questions_future_perfect,
    "Future Perfect Continuous": qt.questions_future_perfect_continuous
}


class Quiz(StatesGroup):
    QuestionIndex = State()


@router0.message(F.text.in_(QUESTION_SETS.keys()))
async def past_answer_1(message: Message, state: FSMContext):
    topic = message.text
    questions = QUESTION_SETS[topic]

    await state.set_state(Quiz.QuestionIndex)
    await state.update_data(correct_answers=0, questions_index=0, topic=topic)
    question = questions[0]
    await message.answer(question['question'], reply_markup=kb.generate_keyboard(question['options']))


@router0.message(Quiz.QuestionIndex)
async def past_answer_2(message: Message, state: FSMContext):
    data = await state.get_data()
    questions = QUESTION_SETS[data['topic']]
    answer = message.text
    correct_answers = data['correct_answers']
    questions_index = data['questions_index']
    correct_answer = questions[questions_index]['correct']

    if answer == correct_answer:
        correct_answers += 1
    questions_index += 1

    if (questions_index < len(questions)):
        await state.update_data(correct_answers=correct_answers, questions_index=questions_index)
        next_question = questions[questions_index]
        await message.answer(next_question['question'], reply_markup=kb.generate_keyboard(next_question['options']))
    else:
        await state.clear()
        await message.answer(
            f"Тест завершен! Вы ответили правильно на {correct_answers} из {len(questions)} вопросов!",
            reply_markup=await main_kb(message.from_user.id))
        if correct_answers == len(questions):
            await rq.update_small_test(message.from_user.id, data['topic'])
            if (await rq.update_big_test(tg_id = message.from_user.id, field_test=data['topic'])):
                await message.answer(f"Ты выполнил все тесты данного времени! Ты получил новое достижение!")
