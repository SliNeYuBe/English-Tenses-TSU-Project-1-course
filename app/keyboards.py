from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Лекции'), KeyboardButton(text='Тесты')],
    [KeyboardButton(text='Профиль'), KeyboardButton(text='Обратная связь')]
],
    resize_keyboard = True,
    input_field_placeholder = 'Выберите пункт меню...')

time = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Past', callback_data='past'),
    InlineKeyboardButton(text = 'Present', callback_data='present'),
    InlineKeyboardButton(text = 'Future', callback_data='future')]
])


category_past = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Simple', callback_data='past_simple'),
    InlineKeyboardButton(text = 'Continuous', callback_data='past_continuous'),
    InlineKeyboardButton(text = 'Perfect', callback_data='past_perfect')],
    [InlineKeyboardButton(text = 'Perfect Continuous', callback_data='past_perfect_continuous')]
])


category_present = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Simple', callback_data='present_simple'),
    InlineKeyboardButton(text = 'Continuous', callback_data='present_continuous'),
    InlineKeyboardButton(text = 'Perfect', callback_data='present_perfect')],
    [InlineKeyboardButton(text = 'Perfect Continuous', callback_data='present_perfect_continuous')]
])


category_future = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Simple', callback_data='future_simple'),
    InlineKeyboardButton(text = 'Continuous', callback_data='future_continuous'),
    InlineKeyboardButton(text = 'Perfect', callback_data='future_perfect')],
    [InlineKeyboardButton(text = 'Perfect Continuous', callback_data='future_perfect_continuous')]
])



tests = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Past'), KeyboardButton(text = 'Present'), KeyboardButton(text = 'Future')],
    [KeyboardButton(text = 'Назад')]
],
    resize_keyboard = True)


past = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Past Simple'), KeyboardButton(text = 'Past Continuous'), KeyboardButton(text = 'Past Perfect')],
    [KeyboardButton(text = 'Past Perfect Continuous')]
],
    resize_keyboard = True)


present = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Present Simple'), KeyboardButton(text = 'Present Continuous'), KeyboardButton(text = 'Present Perfect')],
    [KeyboardButton(text = 'Present Perfect Continuous')]
],
    resize_keyboard = True)


future = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Future Simple'), KeyboardButton(text = 'Future Continuous'), KeyboardButton(text = 'Future Perfect')],
    [KeyboardButton(text = 'Future Perfect Continuous')]
],
    resize_keyboard = True)


main_or_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Вернуться к временам', callback_data='back_time'),
    InlineKeyboardButton(text = 'Пройти тест по данной теме', callback_data='to_time')],
])


async def test_choose(tenses):
    markup = ReplyKeyboardBuilder()
    markup.button(text = tenses)
    markup.button(text = 'Назад')
    markup.adjust(2)
    return markup.as_markup(resize_keyboard = True)



def generate_keyboard(options):
    markup = ReplyKeyboardBuilder()
    for option in options:
        markup.button(text = option)
    markup.adjust(3)
    return markup.as_markup(resize_keyboard=True)
