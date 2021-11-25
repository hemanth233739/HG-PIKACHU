from telethon import events, Button, custom
import re, os
from VegetaRobot.events import register
from VegetaRobot import telethn as tbot
from VegetaRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/a8839c0fdb7da5098b260.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m Pikachu⚡** \n\n"
  PIKACHU += "**♡ I'm Working with awesome speed**\n\n"
  PIKACHU += "**♡ Pikachu : 2.0 LATEST**\n\n"
  PIKACHU += "**♡ My Creator :** [Hemanth](t.me/HEMANTHGAMING1K)\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓🙂", "https://t.me/hgbotsupportgroup"), Button.url("𝐔𝐏𝐃𝐀𝐓𝐄", "https://t.me/hgbotsupdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
