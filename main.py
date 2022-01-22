import discord
import time
from discord.ext import commands

TOKEN = 'NzcxOTE2NDY3NTIzNTUxMjQz.X5zFOw.xaTuS5gErYTbINaSuGtT4dAAQcw'
client = commands.Bot(command_prefix='os.')

@client.command()
async def ping(ctx):
    """
    Get bot's latency.
    """
    start = time.perf_counter()
    message = await ctx.send("Ping?")
    end = time.perf_counter()
    totalping = round((end - start) * 1000)
    embed = discord.Embed(title='Pong!', color=0x57f0f0)
    embed.description = f"**API:** `{round(client.latency * 1000)}` ms\n**RoundTrip:** `{totalping}` ms"
    try:
        await message.edit(content=None, embed=embed)
    except discord.NotFound:
        await ctx.send(embed=embed)

client.run(TOKEN)
