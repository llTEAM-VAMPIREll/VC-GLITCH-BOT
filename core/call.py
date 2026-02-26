
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped

call_instance = None

async def start_call(app):
    global call_instance
    call_instance = PyTgCalls(app)
    await call_instance.start()
    return call_instance

async def join_vc(chat_id, file_path):
    if not call_instance:
        raise Exception("Call instance not started")

    await call_instance.join_group_call(
        chat_id,
        AudioPiped(file_path)
    )

async def leave_vc(chat_id):
    if call_instance:
        await call_instance.leave_group_call(chat_id)
