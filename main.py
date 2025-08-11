import discord
import os
from dotenv import load_dotenv

class MeuPrimeiroBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            intents=intents
        )
        self.tree = discord.app_commands.CommandTree(self)
      
    async def on_ready(self):
        print(f'O bot {self.user} está online!')

# Carrega variáveis do .env
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError('O token do bot não foi encontrado. Defina a variável DISCORD_BOT_TOKEN no arquivo .env')

bot = MeuPrimeiroBot()

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')

bot.run(TOKEN)