from pyrogram import Client

plugins = dict(root="plugins")

app = Client(
    name="Translator",
    plugins=plugins,
    api_id=28933710,
    api_hash="31afd6e672be2836c266320601105119",
    bot_token="7381662296:AAGOoWs62imyeTtO607sLIkpu59vnpBUWpg"
)


app.run()
