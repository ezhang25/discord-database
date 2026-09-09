import discord
import os
from dotenv import load_dotenv

from files import *
from commands import *

load_dotenv()
    
class MyClient(discord.Client):
    user: discord.ClientUser

    async def on_ready(self: MyClient):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("-----")
        self.database = FileSystem()

    async def command_handler(self: MyClient, message: discord.Message):
        message_str = message.content
        message_str = message_str[1:]

        if message_str.startswith('tree'):
            await message.reply(self.database.tree())
        elif message_str.startswith('mkdir'):
            dir_name = message_str[5:]
            dir_name = dir_name.strip()
            if not dir_name.isalnum():
                await message.reply("File names are only allowed letters and numbers")
            if self.database.mkdir(dir_name):
                await message.reply(f"{dir_name} directory was added to {self.database.curr.name}")
            else:
                await message.reply("Failed to add directory")
        elif message_str.startswith('touch'):
            file_name = message_str[5:]
            file_name = file_name.strip()
            if not file_name.isalnum():
                await message.reply("File names are only allowed letters and numbers")
            elif self.database.touch(file_name):
                await message.reply(f"{file_name} file was added to {self.database.curr.name}")
            else:
                await message.reply("Failed to add file")

    async def on_message(self: MyClient, message: discord.Message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$'):
            await self.command_handler(message)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("BOT_TOKEN"))