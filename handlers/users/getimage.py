from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters.builtin import CallbackQuery, Text
from keyboards.inline.menuButton import generateImagesButtons, button
from states.newpost import GetImage
from edit import oneImg, secondImg, threeImg


@dp.callback_query_handler(text='home')
async def test1(call: CallbackQuery):
    lst = ['1', '2', '3', '4']
    await call.answer(cache_time=60)
    image_all = open('images/all.jpg', mode='rb')
    await call.message.answer_photo(photo=image_all, caption="Rasmlardan birini tanlang!",
                                    reply_markup=generateImagesButtons(lst))
    await call.message.delete()


@dp.callback_query_handler(text='back')
async def next(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Assalomu alaykum {call.from_user.full_name}!\n"
                              f"Botdan foydalanish uchun kerakli bo'limni tanlang!", reply_markup=button)
    await call.message.delete()


@dp.callback_query_handler(Text(startswith='⭕'))
async def get_first_image(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    img1 = call.data
    await state.update_data(
        {'image': img1}
    )
    await call.message.answer(f"Endi <em>Ismingizni kiriting: </em>")
    await call.message.delete()
    await GetImage.image.set()

@dp.message_handler(state=GetImage.image)
async def get_user_name(message: types.Message, state: FSMContext):
    name = message.text
    data = await state.get_data()
    data_img1 = data['image']
    if data_img1 == '⭕1':
        photo1 = oneImg(name)
        await message.answer_photo(photo=photo1, caption="Buyurtmangiz tayyor! 😀")
    elif data_img1 == '⭕2':
        photo2 = secondImg(name)
        await message.answer_photo(photo=photo2, caption="Buyurtmangiz tayyor! 😀")
    elif data_img1 == '⭕3':
        photo3 = threeImg(name)
        await message.answer_photo(photo=photo3, caption="Buyurtmangiz tayyor! 😀")
    else:
        await message.answer(f"Kechirasiz siz noto'g'ri tugmani bosidingiz")
    await state.finish()






