from aiogram import Router, types, F

router = Router()

# Продвинутое эхо
@router.message(F.content_type.in_([
    types.ContentType.DOCUMENT,
    types.ContentType.PHOTO,
    types.ContentType.STICKER,
    types.ContentType.VIDEO,
    types.ContentType.TEXT,
    types.ContentType.ANIMATION,
    types.ContentType.VOICE
]))
async def download_doc(message: types.Message):
    if message.document:
        await message.answer_document(message.document.file_id)

    elif message.photo:
        await message.answer_photo(message.photo[-1].file_id)

    elif message.sticker:
        await message.answer_sticker(message.sticker.file_id)

    elif message.video:
        await message.answer_video(message.video.file_id)

    elif message.text:
        await message.answer(message.text)

    elif message.voice:
        await message.answer_voice(message.voice.file_id)