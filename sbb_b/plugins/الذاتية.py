from os import remove

from sbb_b import sbb_b


@sbb_b.ar_cmd(pattern="(جلب الصورة|ذاتية)")
async def datea(event):
    await event.edit("🙂♥️")
    scertpic = await event.get_reply_message()
    downloadjmthon = await scertpic.download_media()
    await sbb_b.send_file("me", downloadjmthon)
    remove(downloadjmthon)
