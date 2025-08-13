from aiogram import Router

router = Router()

from . import commands
from . import keyboard_editing
from . import echo


router.include_router(commands.router)
router.include_router(keyboard_editing.router)
router.include_router(echo.router)