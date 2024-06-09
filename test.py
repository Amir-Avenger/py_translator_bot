from gtts import gTTS
import os

# متنی که می‌خواهید به صوت تبدیل کنید
text = "hi how are you"

# تنظیم زبان (برای فارسی از 'fa' استفاده کنید)
language = 'en'

# ایجاد شیء gTTS
speech = gTTS(text=text, lang=language, slow=False)

# ذخیره فایل صوتی
speech.save("output.mp3")

# پخش فایل صوتی (در صورت نیاز)
os.system("start output.mp3")
