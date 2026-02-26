
from pyrogram import filters
from core.call import join_vc, leave_vc
import os

def register_handlers(app):

    @app.on_message(filters.command("start"))
    async def start(_, message):
        await message.reply("VC Bot Online")

    @app.on_message(filters.command("play"))
    async def play(_, message):
        if len(message.command) < 2:
            return await message.reply("Usage: /play filename.mp3")

        filename = message.command[1]
        file_path = os.path.join("audio", filename)

        if not os.path.exists(file_path):
            return await message.reply("File not found in audio folder")

        try:
            await join_vc(message.chat.id, file_path)
            await message.reply("Playing in VC")
        except Exception as e:
            await message.reply(f"Error: {e}")

    @app.on_message(filters.command("stop"))
    async def stop(_, message):
        await leave_vc(message.chat.id)
        await message.reply("Stopped VC")
