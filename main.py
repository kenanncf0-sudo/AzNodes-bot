import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- Veb Server (7/24 oyaq qalması üçün) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Aznodes Bot 7/24 onlayndır! (Sistem aktivdir)"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()

# --- Discord Bot ---
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Sistem hazır: {bot.user} olaraq giriş edildi!")

@bot.command()
async def salam(ctx):
    await ctx.send("Salam! Mən Aznodes serverinin 7/24 işləyən botuyam!")

# --- Sistemi İşə Salmaq ---
if __name__ == "__main__":
    keep_alive()
    
    # DİQQƏT: Öz botunuzun Tokenini bura daxil edin
    TOKEN = "MTUwMTYwNDQxOTc2OTMzNTg3MA.GpvC77.tpYfdVf7j5guNcwTH3X0AnYmctueMVINuU7QUw"
    
    bot.run(TOKEN)
    
