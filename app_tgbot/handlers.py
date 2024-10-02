from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from app_tgbot.fsm import Form
from app_tgbot.database import SessionLocal, Student


async def start_handler(message: Message, state: FSMContext):
    await message.answer("Hi! What is your name?")
    await state.set_state(Form.name)

async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("How old are your?")
    await state.set_state(Form.age)

async def age_handler(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("What grade are you in?")
    await state.set_state(Form.grade)

async def grade_handler(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    user_data = await state.get_data()

    # save to DB
    session = SessionLocal()
    student = Student(name=user_data['name'], age=int(user_data['age']), grade=user_data['grade'])
    session.add(student)
    session.commit()
    session.close()

    #await message.reply("Your data has been saved successfully!")
    await message.answer(f"*{user_data['name']}*, your data has been saved successfully\!", parse_mode=ParseMode.MARKDOWN_V2)
    # await message.answer(f"<b>{user_data['name']}</b><u>Your data has been saved successfully!</u>", parse_mode="HTML")

    await state.clear()
