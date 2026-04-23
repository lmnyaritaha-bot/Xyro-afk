import discord
from discord.ext import commands
import asyncio

# --- LISTA DIAL L-ACCOUNTS (5 TOKENS) ---
ACCOUNTS = [
    {"token": "TOKEN_1", "voice_id": 1111111111},
    {"token": "TOKEN_2", "voice_id": 2222222222},
    {"token": "TOKEN_3", "voice_id": 3333333333},
    {"token": "TOKEN_4", "voice_id": 4444444444},
    {"token": "TOKEN_5", "voice_id": 5555555555},
]

class MyAFKBot(commands.Bot):
    def __init__(self, token, voice_id):
        super().__init__(command_prefix="!", self_bot=True)
        self.token = token
        self.voice_id = voice_id

    async def on_ready(self):
        print(f'>>> Account khdam: {self.user.name}')
        channel = self.get_channel(self.voice_id)
        if channel:
            try:
                await channel.connect()
                print(f'   [+] {self.user.name} dkhl l-voice!')
            except Exception as e:
                print(f'   [!] Error f {self.user.name}: {e}')

    async def on_voice_state_update(self, member, before, after):
        # Ila t-disconnecta l-bot bo7do, i-reconnecti
        if member.id == self.user.id and after.channel is None:
            print(f'   [R] {self.user.name} t-disconnecta, ghadi n-reconnecti...')
            await asyncio.sleep(5)
            channel = self.get_channel(self.voice_id)
            if channel:
                await channel.connect()

async def start_bots():
    # Ghadi n-lanciwo kolchi f deqqa
    tasks = []
    for acc in ACCOUNTS:
        if acc["token"] != "TOKEN_HERE": # Check bach may-runnich tokens ghalatin
            bot = MyAFKBot(acc["token"], acc["voice_id"])
            tasks.append(bot.start(acc["token"]))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(start_bots())
    except KeyboardInterrupt:
        print("Bot t-tfa.")
      
