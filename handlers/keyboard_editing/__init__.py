from aiogram import Router

router = Router()

from . import en_keyboard_editing
from . import rus_keyboard_editing
from . import keyboard_editing

router.include_router(en_keyboard_editing.router)
router.include_router(rus_keyboard_editing.router)
router.include_router(keyboard_editing.router)