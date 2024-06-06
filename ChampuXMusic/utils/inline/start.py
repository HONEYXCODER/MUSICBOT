from pyrogram.types import InlineKeyboardButton

import config
from ChampuXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="sᴇᴛ", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons

[
            InlineKeyboardButton(text="ᴹᵒʳᵉ ᴮᵒᵗˢ", url=f"https://t.me/+Wora8dGaHoxmOTg1")  ]
