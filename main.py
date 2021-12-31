import os
import discord
import requests
import server
import emojidex
from discord.ext import commands
server.keep_alive()
bot = commands.Bot(command_prefix="#")
credits = {"u1f441_u1f441":512792387274276865,"u1f426_u1f494":512792387274276865,"u1f4ab_u1f4ab":512792387274276865}
def ordinate(*emojitup):
  emojis = emojitup[0]
  for i in range(len(emojis)):
    if emojis[i] == "\u200d":
      emojis[i] = ""
      emojis[i - 1] = ""
    if emojis[i] == "\ufe0f":
      emojis[i] = ""
  emojis = list(filter(None, emojis))
  fin = ""
  for i in emojis:
    fin += str('u{:X}'.format(ord(i)).lower()) + "_"
  fin = fin[:-1]
  return fin
@bot.command()
async def mix(ctx, *emojitup):
  emojis = ""
  for i in emojitup:
    emojis += i
  emojis = list(emojis)
  url = "https://raw.githubusercontent.com/b1nwal/MixerMoji/main/stickers/" + ordinate(emojis) + ".png"
  resp = requests.get(url);
  if (resp.status_code == 404):
    emojis.reverse()
    url = "https://raw.githubusercontent.com/b1nwal/MixerMoji/main/stickers/" + ordinate(emojis) + ".png"
    resp = requests.get(url)
    if (resp.status_code == 404):
      embed = discord.Embed(title="404: Combo Not Found")
      await ctx.send(embed=embed)
      return
    else:
      try:
        credit = credits[ordinate(emojis)]
        credit = await bot.fetch_user(credit)
        av = credit.avatar_url
        credit = credit.name
      except KeyError:
        credit = "Google Emoji Kitchen"
        av = "https://raw.githubusercontent.com/b1nwal/MixerMoji/main/imgs/google_icon.png"
  else:
    try:
      credit = credits[ordinate(emojis)]
      credit = await bot.fetch_user(credit)
      av = credit.avatar_url
      credit = credit.name
    except KeyError:
      credit = "Google Emoji Keyboard"
      av = "https://raw.githubusercontent.com/b1nwal/MixerMoji/main/imgs/google_icon.png"
  embed = discord.Embed(color=0x32a852)
  embed.set_footer(text=credit, icon_url=av)
  embed.set_image(url=url)
  await ctx.send(embed=embed)
@bot.command()
async def index(ctx):
  embed = discord.Embed(title="Compatible Emoji Index",color=0xf542da)
  embed.add_field(name="Most of these emojis *should* work... If they don't send me a help ticket.", value="\u200b",inline=False)
  embed.add_field(name="Faces", value=emojidex.faces,inline=False)
  embed.add_field(name="Faces Cont'd", value=emojidex.faces2,inline=False)
  embed.add_field(name="Animals", value=emojidex.animals, inline=False)
  embed.add_field(name="Miscellaneous", value=emojidex.misc, inline=False)
  await ctx.send(embed=embed)
token = os.environ['token']
bot.run(token)