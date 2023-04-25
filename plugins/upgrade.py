"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 24  ind /🌎 0.3$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 48  ind /🌎 0.6$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 80  ind /🌎 1$  per Month
	
	
	Pay Using Upi I'd ```vasudevareddy187@okhdfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin @sula54321"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/sula54321")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 24  ind /🌎 0.3$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 48  ind /🌎 0.6$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 80  ind /🌎 1$  per Month
	
	
	Pay Using Upi I'd ```vasudevareddy187@okhdfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin @sula54321"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/sula54321")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
