from datetime import datetime, timedelta
from pytz import timezone
import pytz
import discord
import os
import re
import copy
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
rebornHeader = 'Reborn Bot:'
eventChannelId = int(os.environ['channel'])
botToken = os.environ['token']

zakumId = 712803871486902332
scargaId = 713819098961805335
cwkpqId = 711792105361637457
htId = 712393075699220482
apqId = 711765855125373020

timezones = [
	'US/Eastern',
	'US/Pacific',
	'Asia/Singapore',
	'Israel'
]

@bot.event
async def on_ready():
	print('bot is ready')

@bot.command(name="commandList")
async def commandList(ctx):
	#embed = discord.Embed(title="Help", colour = discord.Colour.orange())
	#embed.add_field(name=".zakum" value="Sets a zakum run. Parameters taken is a time in UTC.\n ex of usage: .zakum 0:00", inline=False)
	#embed.add_field(name=".scarga" value="Sets a scarga run. Parameters taken is a time in UTC.\n ex of usage: .scarga 0:00", inline=False)
	#embed.add_field(name=".cwkpq" value="Sets a cwkpq run. Parameters taken is a time in UTC.\n ex of usage: .cwkpq 0:00", inline=False)
	#embed.add_field(name=".ht" value="Sets a horntail run. Parameters taken is a time in UTC.\n ex of usage: .ht 0:00", inline=False)
	#embed.add_field(name=".apq" value="Sets a apq run. Parameters taken is a time in UTC.\n ex of usage: .apq 0:00", inline=False)
	await ctx.send("Help\n" +
		".zakum: Sets a zakum run. Parameters taken is a time in UTC.\n ex of usage: .zakum 0:00\n\n" +
		".scarga: Sets a scarga run. Parameters taken is a time in UTC.\n ex of usage: .scarga 0:00\n\n" +
		".cwkpq: Sets a cwkpq run. Parameters taken is a time in UTC.\n ex of usage: .cwkpq 0:00\n\n" +
		".ht: Sets a horntail run. Parameters taken is a time in UTC.\n ex of usage: .ht 0:00\n\n" +
		".apq: Sets a apq run. Parameters taken is a time in UTC.\n ex of usage: .apq 0:00")

@bot.command()
async def zakum(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime)
	message = await channel.send(f'{rebornHeader}\n<@&{zakumId}> scheduled for {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_b: Bishop\n' +
		':regional_indicator_r: Ranged\n' +
		':regional_indicator_m: Melee\n\n' +
		'Roster:\n' +
		':regional_indicator_b: Bishop:\n' +
		':regional_indicator_r: Ranged:\n' +
		':regional_indicator_m: Melee:\n')
	reactions = ['🇧', '🇷', '🇲']
	for emoji in reactions:
		await message.add_reaction(emoji)

@bot.command()
async def scarga(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime)
	message = await channel.send(f'{rebornHeader}\n<@&{scargaId}> scheduled for {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_b: Bishop\n' +
		':regional_indicator_r: Ranged\n' +
		':regional_indicator_m: Melee'
		#'Roster:\n' +
		#':regional_indicator_b: Bishop:\n' +
		#':regional_indicator_r: Ranged:\n' +
		#':regional_indicator_m: Melee:\n'
		)
	reactions = ['🇧', '🇷', '🇲']
	for emoji in reactions:
		await message.add_reaction(emoji)

@bot.command()
async def cwkpq(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime)
	message = await channel.send(f'{rebornHeader}\n<@&{cwkpqId}> scheduled for {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_a: Archer\n' +
		':regional_indicator_w: Warrior\n' +
		':regional_indicator_m: Mage\n' +
		':regional_indicator_p: Pirate\n' +
		':regional_indicator_t: Thief'
		#'Roster:\n' +
		#':regional_indicator_a: Archer\n' +
		#':regional_indicator_w: Warrior\n' +
		#':regional_indicator_m: Mage\n' +
		#':regional_indicator_p: Pirate\n' +
		#':regional_indicator_t: Thief\n\n' +
		)
	reactions = ['🇦', '🇼', '🇲', '🇵', '🇹']
	for emoji in reactions:
		await message.add_reaction(emoji)
	rewardMsg = await channel.send('Also react for PQ reward\n' +
		':regional_indicator_m: MON/Payout\n' +
		':regional_indicator_b: Bonus')
	rewardReactions = ['🇲', '🇧']
	for emoji in rewardReactions:
		await rewardMsg.add_reaction(emoji)

@bot.command()
async def ht(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime)
	message = await channel.send(f'{rebornHeader}\n<@&{htId}> scheduled for {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_b: Bishop\n' +
		':regional_indicator_s: Seduce\n' +
		':regional_indicator_a: Attacker\n'
		#'Roster:\n' +
		#':regional_indicator_a: Archer\n' +
		#':regional_indicator_w: Warrior\n' +
		#':regional_indicator_m: Mage\n' +
		#':regional_indicator_p: Pirate\n' +
		#':regional_indicator_t: Thief\n\n' +
		)
	reactions = ['🇧', '🇸', '🇦']
	for emoji in reactions:
		await message.add_reaction(emoji)

@bot.command()
async def apq(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime)
	message = await channel.send(f'{rebornHeader}\n<@&{apqId}> scheduled for {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_b: Bride\n' +
		':regional_indicator_g: Groom'
		)
	reactions = ['🇧', '🇬']
	for emoji in reactions:
		await message.add_reaction(emoji)

def validateInput(stringTime, timeZone):
	time_re = re.compile(r'^\d?\d:\d\d$')
	return True if time_re.match(stringTime) and timezoneDict.get(timeZone) != None else False

def utcToLocalizedTzs(inputTime):
	input_time_obj = datetime.strptime(inputTime, '%H:%M')
	time_now = datetime.now(tz=pytz.utc) # offset aware datetime
	scheduled_utc_time = time_now.replace(
			hour=input_time_obj.hour,
			minute=input_time_obj.minute,
			second=0,
			microsecond=0,
		)
	# assume scheduled time needs to be in the future
	if scheduled_utc_time < time_now:
		scheduled_utc_time + timedelta(days=1)

	localizedTimes = [
		('• ' + scheduled_utc_time.astimezone(pytz.timezone(tz)).strftime('%H:%M') + ' ' + tz) for tz in timezones
	]
	return '**Localized Timezones:** \n' + "\n".join(localizedTimes) + '\n\n'

bot.run(botToken)