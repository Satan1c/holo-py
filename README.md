# holo-py

## Установка

* В кореневую папку проэкта, или в папку билиотек, скопировать папку holo_py

# Внимание!
## Враппер полностью асинхронен. Любые вызовы функций следует проводить только в асинхронных функциях

## Использование на практике с discord.py
```py
from discord import Message, Embed, Client
from holo_py import HoloClient

bot = Client()
holo = HoloClient(bot.loop)

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_message(message: Message):
    if not message.author.bot:
        resp = await holo.get_emote(message.content if len(message.content) >= 3 else "kiss")

        embed = Embed()
        embed.set_image(url=resp.url)

        await message.channel.send(embed=embed)

bot.run("discord-bot token")
```
