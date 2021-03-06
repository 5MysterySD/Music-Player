"""
RadioPlayerV2, Telegram Voice Chat Userbot
Copyright (C) 2021  Asm Safone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "ðð» **Hey [{}](tg://user?id={})**,\n\nI'm **Radio & Music Player Bot** \nI Can Play Radio/Stream Music In Channels & Groups 24x7 Nonstop. \nModified with â¤ï¸ By @MysterySD!"
HELP = """  â­ââââãð **<i>HELP GUIDE</i>** ã
 â
 âð **Common Commands For You**:
 â
 â \u2022 `/play` reply to an audio to play or queue it
 â \u2022 `/help` shows help for commands
 â \u2022 `/playlist` shows the playlist
 â \u2022 `/current` shows playing time of current track
 â \u2022 `/song` [song name] download the song as audio
 â
 âð **Admin Commands [â ï¸Not For Youâ ï¸]**:
 â
 â \u2022 `/skip` [n] skip current or n where n >= 2
 â \u2022 `/join` join voice chat of current group
 â \u2022 `/leave` leave current voice chat
 â \u2022 `/vc` check which VC is joined
 â \u2022 `/stop` stop playing music
 â \u2022 `/radio` start radio stream
 â \u2022 `/stopradio` stop radio stream
 â \u2022 `/replay` play from the beginning
 â \u2022 `/clean` remove unused RAW PCM files
 â \u2022 `/pause` pause playing music
 â \u2022 `/resume` resume playing music
 â \u2022 `/mute` mute the VC userbot
 â \u2022 `/unmute` unmute the VC userbot
 â \u2022 `/restart` restart the bot
 â
 âð¥ **ð¨âð» DEV ð¨âð»: @MysterySD** ð§
 â
 â°âââââã â¡<i> @Infyplex </i>â¡ ã
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('ðCHANNELð', url='https://t.me/Infyplex'),
        InlineKeyboardButton('âï¸SUPPORTâï¸', url='https://t.me/MF_Support'),
    ],
    [
        InlineKeyboardButton('ð¯ HELP ð¯', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
