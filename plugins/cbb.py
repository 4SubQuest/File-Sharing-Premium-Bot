# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○   Oᴡɴᴇʀ - </b> <a href='tg://user?id={OWNER_ID}'>Mᴏɴᴋᴇʏ D Lᴜғғʏ</a> \n<b>○   Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/AnimeQuestX'>Aɴɪᴍᴇ Qᴜᴇsᴛ</a> \n<b>○   Hɪɴᴅɪ Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/AnimeQuestHindi'>Aɴɪᴍᴇ Qᴜᴇsᴛ Hɪɴᴅɪ</a> \n<b>○   Oɴɢᴏɪɴɢ Cʜᴀɴɴᴀʟ - </b> <a href='https://t.me/OngoingAnimeQuest'>Oɴɢᴏɪɴɢ Aɴɪᴍᴇ Qᴜᴇsᴛ</a> \n<b>○   Dɪsᴄᴜssᴛɪᴏɴ Gʀᴏᴜᴘ - </b> <a href='https://t.me/+r-x-wA4JT5gxZjVl'>Aɴɪᴍᴇ Qᴜᴇsᴛ Cʜᴀᴛ</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
