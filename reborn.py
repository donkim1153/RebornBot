from datetime import datetime, timedelta, date
from pytz import timezone
import pytz
import discord
import os
import re
import copy
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = '.')
rebornHeader = 'Reborn Bot:'
eventChannelId = int(os.environ['channel'])
botToken = os.environ['token']

zakumId = 712803871486902332
scargaId = 713819098961805335
cwkpqId = 711792105361637457
htId = 712393075699220482
apqId = 711765855125373020
gpqId = 712778006208184320


timezones = [	
	'US/Pacific',
	'US/Eastern',
	'Asia/Singapore',
	'Australia/Sydney',
	'Israel'
]

eventDict = {
	'zakum': zakumId,
	'scarga': scargaId,
	'cwkpq': cwkpqId,
	'ht': htId,
	'apq': apqId,
	'gpq': gpqId
}

eventTracker = {
	'zakum': {},
	'scarga': {},
	'cwkpq': {},
	'ht': {},
	'apq': {},
	'gpq': {}
}


@bot.event
async def on_ready():
	print('bot is ready', flush=True)

@bot.command(name="commandList")
async def commandList(ctx):
	#embed = discord.Embed(title="Help", colour = discord.Colour.orange())
	#embed.add_field(name=".zakum" value="Sets a zakum run. Parameters taken is a time in UTC.\n ex of usage: .zakum 0:00", inline=False)
	#embed.add_field(name=".scarga" value="Sets a scarga run. Parameters taken is a time in UTC.\n ex of usage: .scarga 0:00", inline=False)
	#embed.add_field(name=".cwkpq" value="Sets a cwkpq run. Parameters taken is a time in UTC.\n ex of usage: .cwkpq 0:00", inline=False)
	#embed.add_field(name=".ht" value="Sets a horntail run. Parameters taken is a time in UTC.\n ex of usage: .ht 0:00", inline=False)
	#embed.add_field(name=".apq" value="Sets a apq run. Parameters taken is a time in UTC.\n ex of usage: .apq 0:00", inline=False)
	await ctx.send("Event List: [zakum, scarga, cwkpq, ht, apq, gpq]\n\n" +
		".{event}: Sets an event run. Parameters: time (required, hh:mm in UTC), date (optional, mm-dd)\n\n" + 
		"Example usage:\n" +
		".zakum 0:00\n" +
		".scarga 2:00 7-23\n\n"
		)

@bot.command()
async def zakum(ctx, inputTime, inputDate=str(date.today())[5:]):
	if (validateInput(inputTime, inputDate) == False):
		await ctx.send("Please ensure your inputs are in the format time=##:##, date=MM-DD (date is optional)")
		raise Exception("Invalid input")
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime, inputDate)
	time_object = generateTimeObject(inputTime, inputDate)
	#print(inputDate, flush=True)
	message = await channel.send(f'{rebornHeader}\n<@&{zakumId}> scheduled for ' + 
		time_object.strftime('%m/%d').lstrip('0').replace('/0','/') + 
		f' - {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_b: Bishop\n' +
		':regional_indicator_r: Ranged\n' +
		':regional_indicator_m: Melee\n\n' 
		#'Roster:\n' +
		#':regional_indicator_b: Bishop:\n' +
		#':regional_indicator_r: Ranged:\n' +
		#':regional_indicator_m: Melee:\n'
		)
	#reactions = ['🇧', '🇷', '🇲']
	#for emoji in reactions:
		#await message.add_reaction(emoji)
	eventTracker['zakum'][message.id] = time_object

@bot.command()
async def scarga(ctx, inputTime, inputDate=str(date.today())[5:]):
	if (validateInput(inputTime, inputDate) == False):
		await ctx.send("Please ensure your inputs are in the format time=##:##, date=MM-DD (date is optional)")
		raise Exception("Invalid input")
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime, inputDate)
	time_object = generateTimeObject(inputTime, inputDate)
	message = await channel.send(f'{rebornHeader}\n<@&{scargaId}> scheduled for ' + 
		time_object.strftime('%m/%d').lstrip('0').replace('/0','/') + 
		f' - {inputTime} UTC.\n\n' +
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
	#reactions = ['🇧', '🇷', '🇲']
	#for emoji in reactions:
		#await message.add_reaction(emoji)
	eventTracker['scarga'][message.id] = time_object

@bot.command()
async def cwkpq(ctx, inputTime, inputDate=str(date.today())[5:]):
	if (validateInput(inputTime, inputDate) == False):
		await ctx.send("Please ensure your inputs are in the format time=##:##, date=MM-DD (date is optional)")
		raise Exception("Invalid input")
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime, inputDate)
	time_object = generateTimeObject(inputTime, inputDate)
	message = await channel.send(f'{rebornHeader}\n<@&{cwkpqId}> scheduled for ' + 
		time_object.strftime('%m/%d').lstrip('0').replace('/0','/') + 
		f' - {inputTime} UTC.\n\n' +
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
	#reactions = ['🇦', '🇼', '🇲', '🇵', '🇹']
	#for emoji in reactions:
		#await message.add_reaction(emoji)
	rewardMsg = await channel.send('Also react for PQ reward\n' +
		':regional_indicator_m: MON/Payout\n' +
		':regional_indicator_b: Bonus')
	#rewardReactions = ['🇲', '🇧']
	#for emoji in rewardReactions:
		#await rewardMsg.add_reaction(emoji)
	eventTracker['cwkpq'][message.id] = time_object

@bot.command()
async def ht(ctx, inputTime, inputDate=str(date.today())[5:]):
	if (validateInput(inputTime, inputDate) == False):
		await ctx.send("Please ensure your inputs are in the format time=##:##, date=MM-DD (date is optional)")
		raise Exception("Invalid input")
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime, inputDate)
	time_object = generateTimeObject(inputTime, inputDate)
	message = await channel.send(f'{rebornHeader}\n<@&{htId}> scheduled for ' + 
		time_object.strftime('%m/%d').lstrip('0').replace('/0','/') + 
		f' - {inputTime} UTC.\n\n' +
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
	#reactions = ['🇧', '🇸', '🇦']
	#for emoji in reactions:
		#await message.add_reaction(emoji)
	eventTracker['ht'][message.id] = time_object

@bot.command()
async def apq(ctx, inputTime, inputDate=str(date.today())[5:]):
	if (validateInput(inputTime, inputDate) == False):
		await ctx.send("Please ensure your inputs are in the format time=##:##, date=MM-DD (date is optional)")
		raise Exception("Invalid input")
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime, inputDate)
	time_object = generateTimeObject(inputTime, inputDate)
	message = await channel.send(f'{rebornHeader}\n<@&{apqId}> scheduled for ' + 
		time_object.strftime('%m/%d').lstrip('0').replace('/0','/') + 
		f' - {inputTime} UTC.\n\n' +
		localized_times +
		'Please react with the following to sign up:\n' +
		':regional_indicator_b: Bride\n' +
		':regional_indicator_g: Groom'
		)
	#reactions = ['🇧', '🇬']
	#for emoji in reactions:
		#await message.add_reaction(emoji)
	eventTracker['apq'][message.id] = time_object
	
@bot.command()
async def gpq(ctx, inputTime, inputDate=str(date.today())[5:]):
	if (validateInput(inputTime, inputDate) == False):
		await ctx.send("Please ensure your inputs are in the format time=##:##, date=MM-DD (date is optional)")
		raise Exception("Invalid input")
	channel = bot.get_channel(eventChannelId)
	localized_times = utcToLocalizedTzs(inputTime, inputDate)
	time_object = generateTimeObject(inputTime, inputDate)
	message = await channel.send(f'{rebornHeader}\n<@&{gpqId}> scheduled for ' + 
		time_object.strftime('%m/%d').lstrip('0').replace('/0','/') + 
		f' - {inputTime} UTC.\n\n' +
		localized_times + 
		'Please react with the following to sign up:\n' +
		':regional_indicator_m: Mage\n' +
		':regional_indicator_t: Thief\n' +
		':regional_indicator_n: Noob (low level char)\n' +
		':regional_indicator_o: Other\n'
		)
	#reactions = ['🇲', '🇹', '🇳', '🇴']
	#for emoji in reactions:
		#await message.add_reaction(emoji)
		#print('adding emoji')
	eventTracker['gpq'][message.id] = time_object
	

@bot.event
async def on_message_delete(message):
	#print(message, flush=True)
	for event, dict in eventTracker.items():
		if dict:
			temp_list = []
			for id in dict.keys():
				if id == message.id:
					temp_list.append(id)
			for id in temp_list:
				del eventTracker[event][id]
					


def validateInput(stringTime, timeZone):
	time_re = re.compile(r'^\d?\d:\d\d$')
	return True if time_re.match(stringTime) and timezoneDict.get(timeZone) != None else False

def generateTimeObject(inputTime, inputDate):
	input_time_obj = datetime.strptime(inputTime, '%H:%M')
	input_date_obj = datetime.strptime(inputDate, '%m-%d')
	time_now = datetime.now(tz=pytz.utc) # offset aware datetime
	scheduled_utc_time = time_now.replace(
			month=input_date_obj.month,
			day=input_date_obj.day,
			hour=input_time_obj.hour,
			minute=input_time_obj.minute,
			second=0,
			microsecond=0,
		)
	# assume scheduled time needs to be in the future
	while scheduled_utc_time < time_now:
		scheduled_utc_time = scheduled_utc_time + timedelta(days=1)
	
	#print(scheduled_utc_time, flush=True)
	return scheduled_utc_time

def utcToLocalizedTzs(inputTime, inputDate):
	scheduled_utc_time = generateTimeObject(inputTime, inputDate)
	
	localizedTimes = [
		('• ' + scheduled_utc_time.astimezone(pytz.timezone(tz)).strftime('%m/%d - %H:%M').lstrip('0').replace('/0', '/') + ' ' + tz) for tz in timezones
	]
	return '**Localized Timezones:** \n' + "\n".join(localizedTimes) + '\n\n'
	
def validateInput(inputTime, inputDate):
	print('validating string', flush=True);
	time_re = re.compile(r'^\d?\d:\d\d$')
	date_re = re.compile(r'\d{1,2}-\d{1,2}')
	
	return True if time_re.match(inputTime) and date_re.match(inputDate) else False

async def checkEvents():
	await bot.wait_until_ready()
	while True:
		#print('checking events',flush=True)
		time_now = datetime.now(tz=pytz.utc)
		for event, dict in eventTracker.items():
			if dict:
				temp_list = []
				for id, t in dict.items():
					#print(t, flush=True)
					if t - timedelta(minutes=15) < time_now:
						temp_list.append(id)
						await reminder(eventDict.get(event))
				for id in temp_list:
					del eventTracker[event][id]
		#print('finished checking events', flush=True)
		await asyncio.sleep(60)

async def reminder(eventId):
	channel = bot.get_channel(eventChannelId)
	await channel.send(f'{rebornHeader}\nReminder, <@&' + str(eventId) + '> starting in 15 minutes!\n')


bot.loop.create_task(checkEvents())
bot.run(botToken)
