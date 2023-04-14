from aiogram.dispatcher.filters.state import StatesGroup, State


class GetImage(StatesGroup):
    image = State()

