import os
import discord
import requests
import server
from discord.ext import commands
server.keep_alive()
bot = commands.Bot(command_prefix="#")
edgecases = {"👁️": "u1f441"}
emojisfaces = ":grinning: :grin: :joy: :smiley: :smile: :sweat_smile: :laughing: :innocent: :smiling_imp: :imp: :wink: :blush: :yum: :relieved: :heart_eyes: :sunglasses: :smirk: :neutral_face: :expressionless: :unamused: :sweat: :pensive: :white_frowning_face: :relaxed: :confused: :confounded: :kissing: :kissing_heart: :kissing_smiling_eyes: :kissing_closed_eyes: :smiling_face_with_3_hearts: :yawning_face: :smiling_face_with_tear: :stuck_out_tongue: :stuck_out_tongue_winking_eye: :stuck_out_tongue_closed_eyes: :disappointed: :worried: :angry: :rage: :cry: :persevere: :triumph: :disappointed_relieved: :frowning: :anguished: :fearful: :weary: :sleepy: :tired_face:"
emojisfaces2 = ":grimacing: :sob: :open_mouth: :cold_sweat: :scream: :astonished: :flushed: :sleeping: :dizzy_face: :face_with_spiral_eyes: :no_mouth: :face_in_clouds: :mask: :partying_face: :woozy_face: :hot_face: :cold_face: :disguised_face: :pleading_face: :face_with_monocle: :slightly_frowning_face: :slightly_smiling_face: :upside_down_face: :face_with_rolling_eyes: :zipper_mouth_face: :money_mouth_face: :face_with_thermometer: :nerd_face: :thinking_face: :face_with_head_bandage: :robot_face: :hugging_face: :face_with_cowboy_hat: :clown_face: :nauseated_face: :rolling_on_the_floor_laughing: :drooling_face: :lying_face: :sneezing_face: :face_with_raised_eyebrow: :star_struck: :zany_face: :shushing_face: :face_with_symbols_over_mouth: :face_with_hand_over_mouth: :face_vomiting: :exploding_head:"
emojisanimals = ":mouse2: :rabbit2: :cat2: :snail: :goat: :monkey: :pig2: :octopus: :bee: :fish: :turtle: :bird: :koala: :lion_face: :scorpion: :unicorn_face: :bat: :owl: :deer: :hedgehog: :llama: :sloth: :spider: :teddy_bear: :mouse: :rabbit: :cat: :monkey_face: :pig: :bear: :panda_face: :pig_nose: :smile_cat: :joy_cat: :smiley_cat: :heart_eyes_cat: :smirk_cat: :kissing_cat: :pouting_cat: :crying_cat_face: :scream_cat: :see_no_evil: :hear_no_evil: :speak_no_evil:"
emojismisc = ":sunny: :cloud: :snowman2: :snowman: :coffee: :skull_and_crossbones: :sparkles: :snowflake: :star: :cityscape: :night_with_stars: :city_sunset: :city_sunrise: :rainbow: :earth_africa: :earth_americas: :earth_asia: :globe_with_meridians: :first_quarter_moon_with_face: :last_quarter_moon_with_face: :sun_with_face: :star2: :stars: :cloud_tornado: :hotdog: :evergreen_tree: :cactus: :tulip: :cherry_blossom: :rose: :blossom:    :lemon: :pineapple: :strawberry: :bread: :fork_and_knife: :fork_knife_plate: :birthday: :jack_o_lantern: :christmas_tree: :balloon: :tada: :confetti_ball: :reminder_ribbon: :carousel_horse: :fishing_pole_and_fish: :headphones: :notes: :musical_score: :microbe: :crown: :ghost: :alien: :skull: :kiss: :love_letter: :gem: :bouquet: :zzz: :sweat_drops: :dash: :hankey: :dizzy: :100: :newspaper: :crystal_ball: :hole: :dark_sunglasses: :avocado: :baguette_bread: :cheese_wedge: :cupcake: :adhesive_bandage: :magic_wand: :feather:"
credits = {"u1f441_u1f441":512792387274276865,"u1f426_u1f494":512792387274276865,"u1f4ab_u1f4ab":512792387274276865}
def ordinate(*emojitup):
  emojis = emojitup[0]
  for i in range(len(emojis)):
    if emojis[i] == "\u200d":
      emojis[i] = ""
      emojis[i - 1] = ""
  emojis = list(filter(None, emojis))
  fin = ""
  for i in emojis:
    try:
      fin += str('u{:X}'.format(ord(i)).lower()) + "_"
    except TypeError:
      fin += edgecases[i] + "_"
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
      await ctx.send("`404` Combo not found")
      return
    else:
      try:
        credit = credits[ordinate(emojis)]
        credit = await bot.fetch_user(credit)
        credit = credit.name
      except KeyError:
        credit = "Google Emoji Kitchen"
  else:
    try:
      credit = credits[ordinate(emojis)]
      credit = await bot.fetch_user(credit)
      credit = credit.name
    except KeyError:
      credit = "Google Emoji Keyboard"
  embed = discord.Embed()
  embed.set_author(name=credit)
  embed.set_image(url=url)
  await ctx.send(embed=embed)
@bot.command()
async def index(ctx):
  embed = discord.Embed(title="Compatible Emoji Index")
  embed.add_field(name="Most of these emojis *should* work... If they don't send me a help ticket.", value="\u200b",inline=False)
  embed.add_field(name="Faces", value=emojisfaces,inline=False)
  embed.add_field(name="Faces 2", value=emojisfaces2,inline=False)
  embed.add_field(name="Animals", value=emojisanimals, inline=False)
  embed.add_field(name="Miscellaneous", value=emojismisc, inline=False)
  await ctx.send(embed=embed)
token = os.environ['token']
bot.run(token)