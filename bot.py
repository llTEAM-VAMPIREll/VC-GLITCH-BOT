
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from core.call import start_call
from core.handlers import register_handlers

app = Client(
    "vcbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    await app.start()
    await start_call(app)
    register_handlers(app)
    print("Bot Started Successfully")
    await app.idle()

if __name__ == "__main__":
    asyncio.run(main())
