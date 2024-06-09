from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ReplyKeyboardMarkup
from googletrans import Translator
from gtts import gTTS
import os


@Client.on_message(filters.command("start"))
def start_message(Client, message):
    message.reply_text(f"""سلام {message.from_user.first_name}
به ربات مترجم خوش آمدی 
لطفا زبان مقصد رو انتخاب کن ( زبان ورودی شناسایی میشود )
                       """,
                       reply_markup=InlineKeyboardMarkup(
                           [
                               [
                                    InlineKeyboardButton(text="انگلیسی", callback_data="en"),
                                    InlineKeyboardButton(text="عربی", callback_data="ar"),
                                    InlineKeyboardButton(text="فرانسه", callback_data="fr"),
                                    InlineKeyboardButton(text="فارسی", callback_data="fa"),
                               ],
                               [
                                    InlineKeyboardButton(text="ایتالیایی", callback_data="it"),
                                    InlineKeyboardButton(text="ترکی", callback_data="tr"),
                                    InlineKeyboardButton(text="چینی", callback_data="zh-cn"),
                                    InlineKeyboardButton(text="کره ای", callback_data="ko"),
                               ]
                           ]
                       ))

def second_message(Client, message):
    message.reply_text("برای تغییر زیان زبان مورد نظر را انتخاب کتید در غیر این صورت متن خود را وارد کنید ",
                       reply_markup=InlineKeyboardMarkup(
                           [
                               [
                                    InlineKeyboardButton(text="انگلیسی", callback_data="en"),
                                    InlineKeyboardButton(text="عربی", callback_data="ar"),
                                    InlineKeyboardButton(text="فرانسه", callback_data="fr"),
                                    InlineKeyboardButton(text="فارسی", callback_data="fa"),
                               ],
                               [
                                    InlineKeyboardButton(text="ایتالیایی", callback_data="it"),
                                    InlineKeyboardButton(text="ترکی", callback_data="tr"),
                                    InlineKeyboardButton(text="چینی", callback_data="zh-cn"),
                                    InlineKeyboardButton(text="کره ای", callback_data="ko"),
                               ]
                           ]
                       ))

lang = ""
@Client.on_callback_query()
def select_lang (Client,callback):
    global lang
    lang = callback.data
    response_text = "زبان مورد نظر انتخاب شد . متن خود را وارد کنید "
    Client.send_message(chat_id=callback.from_user.id, text=response_text)
    callback.answer()
    
user_text = ""
translator = Translator()
def translated(lang,user_text):
    trans = translator.translate(text=user_text, dest=lang)
    return trans.text

def convert_voice(Client,message,lang,user_text):
    global audio_file
    speech = gTTS(text=user_text,lang=lang, slow=False)
    audio_file = "user_message.mp3"
    speech.save(audio_file)
    message.reply_voice(audio_file)
    


@Client.on_message(filters.text)
def save_text(Client,message):
    global user_text
    user_text = message.text
    tranlated = translated(lang,user_text)
    message.reply_text(tranlated)
    convert_voice(Client=Client,message=message,lang=lang,user_text=tranlated)
    second_message(Client,message)
    os.remove(audio_file)


    