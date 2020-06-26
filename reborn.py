import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
rebornHeader = 'Reborn Bot:'
eventChannelId = os.environ['channel']
botToken = os.environ['token']

@bot.event
async def on_ready():
	print('bot is ready')

@bot.command()
async def zakum(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	message = await channel.send(f'{rebornHeader}\nZakum scheduled for {inputTime} UTC.\n\n' + 
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
	message = await channel.send(f'{rebornHeader}\nScarga scheduled for {inputTime} UTC.\n\n' + 
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
	message = await channel.send(f'{rebornHeader}\nCWKPQ scheduled for {inputTime} UTC.\n\n' + 
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
		':regional_indicator_b Bonus')
	rewardReactions = ['🇲', '🇧']
	for emoji in rewardReactions:
		await rewardMsg.add_reaction(emoji)

@bot.command()
async def ht(ctx, inputTime):
	channel = bot.get_channel(eventChannelId)
	message = await channel.send(f'{rebornHeader}\nScarga scheduled for {inputTime} UTC.\n\n' + 
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

bot.run(botToken)