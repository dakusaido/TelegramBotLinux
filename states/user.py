from aiogram.dispatcher.filters.state import StatesGroup, State

__all__ = ['RegUser', 'HandAdditionLocation']


class RegUser(StatesGroup):
    reg_user = State()


class HandAdditionLocation(StatesGroup):
    name = State()
    location = State()
    img = State()
    img_ = State()
    info = State()
    info_ = State()
    cancel = State()
