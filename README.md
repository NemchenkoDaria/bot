# Quiz bot
Бот с небольшим квизом
# Name
https://t.me/Braindo_bot
# Описание команд 
### Команда /start
Выводит приветсвенное сообщение: "Добро пожаловать в квиз!". Добавлена кнопка "Начать игру".

    @router.message(Command("start"))
    async def cmd_start(message: types.Message):
        builder = ReplyKeyboardBuilder()
        builder.add(types.KeyboardButton(text="Начать игру"))
        await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))
### Команда /quiz
После нажатия кнопки "Начать игру" выводится сообщение "Давайте начнем квиз!". И после этого бот задаёт вам вопросы.

    @router.message(F.text=="Начать игру")
    @router.message(Command("quiz"))
    async def cmd_quiz(message: types.Message):
        await message.answer(f"Давайте начнем квиз!")
        await new_quiz(message)
