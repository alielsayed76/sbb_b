from sbb_b import sbb_b 

from ..core.managers import edit_or_reply

plugin_category = "fun"


@sbb_b.ar_cmd(
    pattern="وصلت$",
    command=("وصلت", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}join",
    },
)
async def _(event):
    "fun art"
    await edit_or_reply(
        event,
        "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ انا لما انت جيت \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`",
    )


@sbb_b.ar_cmd(
    pattern="علي$",
    command=("علي", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}climb",
    },
)
async def _(event):
    "fun art"
    await edit_or_reply(
        event, "⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿\n"
"⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"
"⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠻⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"
"⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
"⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠸⣿⣿⣿\n"
"⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠀⠤⠄⠀⠀⠉⠁⠀⠀⠀⢿⣿⣿\n"
"⣿⣿⣿⣿⠀⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠠⣿⣿⣷⠀⣿⣿\n"
"⣿⣿⣿⣿⡀⠀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠉⠉⠁⠀⣿⣿\n"
"⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿\n"
"⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿\n"
"⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
"⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿🅿🅾🅺🅴🅼🅾🅽⢸⣿⣿⣿⣿⣿⣿\n"
"🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️🅲🅷🆄\n"
    )


@sbb_b.ar_cmd(
    pattern="هووف$",
    command=("هووف", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}aag",
    },
)
async def _(event):
    "fun art"
    await edit_or_reply(event, "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`")


@sbb_b.ar_cmd(
    pattern="ادفع$",
    command=("ادفع", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}push",
    },
)
async def _(event):
    "fun art"
    await edit_or_reply(
        event,
        "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`",
    )


@sbb_b.ar_cmd(
    pattern="مذكرة$",
    command=("مذكرة", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}work",
    },
)
async def _(event):
    "fun art"
    await edit_or_reply(
        event, "`📔📚             📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    )


@sbb_b.ar_cmd(
    pattern="قمرات$",
    command=("قمرات", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}lmoon",
    },
)
async def test(event):
    "fun art"
    await edit_or_reply(
        event,
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕",
    )


@sbb_b.ar_cmd(
    pattern="مدينه$",
    command=("مدينه", plugin_category),
    info={
        "header": "Fun art.",
        "usage": "{tr}city",
    },
)
async def test(event):
    "fun art"
    await edit_or_reply(
        event,
        """☁️☁️☁️🌞      ☁️     ☁️  ☁️ ☁️
  ☁️ ☁️  ✈️    ☁️    🚁    ☁️    ☁️            
☁️  ☁️    ☁️       ☁️     ☁️   ☁️ ☁️
       🏬🏨🏫🏢🏤🏥🏦🏪🏫
         🌲/         l🚍  \🌳👭
        🌳/  🚘  l 🏃   \🌴 👬                       
 👬🌴/          l  🚔    \🌲
     🌲/   🚖   l              \                               
   🌳/🚶        |   🚍     \ 🌴🚴🚴
  🌴/               |                \🌲""",
    )
