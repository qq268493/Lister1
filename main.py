token = "6924145075:AAGqMlHBm3CmegXs3_BvHsTMXGK6uDuLdyM"
ownerID = int("1961752558")

import asyncio,requests
from pyromod import listen
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from kvsqlite.sync import Client as DB
from datetime import date
from pyrogram.errors import FloodWait 
botdb = DB('bottdgb.sqlite')

bot = Client(
  'bot'+token.split(":")[0],
  9398500, 
 'ad2977d673006bed6e5007d953301e13',
  bot_token=token, in_memory=True
)
app = Client(
  'bkakot',
  9398500, 
 'ad2977d673006bed6e5007d953301e13',
  bot_token=token, in_memory=True
)
headers = {
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.clashofstats.com/',
    'DNT': '1',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

async def Clash(idd):
    params = {
        'q': idd,
        'page': '0',
        'nameEquality': 'false',
    }
    response = requests.get('https://api.clashofstats.com/search/players', params=params, headers=headers).json()
    print(response)
    name = response['items'][0]['name']
    id = response['items'][0]['tag']
    expLevel = response['items'][0]['expLevel']
    clanName = response['items'][0]['clanName']
    town = response['items'][0]['townHallLevel']
    war = response['items'][0]['warStars']
    
    text = f"*اسم الحساب : {name} \nهاشتاك الحساب : {id} .\nاسم الكلان : {clanName} \nمستوى الخبرة للحساب: {expLevel} \nمستوى قاعة المدينة: {town} \nنجوم الحرب للحساب : {war} *"
    
    return text
async def english(idd):
    params = {
        'q': idd,
        'page': '0',
        'nameEquality': 'false',
    }
    response = requests.get('https://api.clashofstats.com/search/players', params=params, headers=headers).json()
    print(response)
    name = response['items'][0]['name']
    id = response['items'][0]['tag']
    expLevel = response['items'][0]['expLevel']
    clanName = response['items'][0]['clanName']
    town = response['items'][0]['townHallLevel']
    war = response['items'][0]['warStars']
    
    text = f"""**
Name : {name}
Hash : {id}
ClanName : {clanName}
ExpLevel: {expLevel}
TwonHall: {town}
starts war: {war} **"""
    return text
async def clans(hash):
	req = requests.get(f'https://api.clashofstats.com/clans/{hash}').json()
	print(req)
	tag = req['tag']
	name = req['name']
	description = req['description']
	level = req['clanLevel']
	winst = req['warWinStreak']
	win = req['warWins']
	mem = req['members']
	try:
		lost = req['warLosses']
		text = f"""**
	Name clan : {name}
	Hash clan : {tag}
	Level clan : {level}
	Member clan :{mem}
	description :{description}
	warWinStreak : {winst}
	Win war:{win}
	warLosses : {lost}
	**"""
	except KeyError:
		text = f"""**
	Name clan : {name}
	Hash clan : {tag}
	Level clan : {level}
	Member clan  :{mem}
	description :{description}
	warWinStreak : {winst}
	Win war:{win}
	**"""
	return text
async def ns(hash):
	req = requests.get(f'https://api.clashofstats.com/clans/{hash}').json()
	print(req)
	tag = req['tag']
	name = req['name']
	description = req['description']
	level = req['clanLevel']
	winst = req['warWinStreak']
	win = req['warWins']
	mem = req['members']
	try:
		lost = req['warLosses']
		text = f"""**
	اسم الكلان : {name}
	هاشتاك : {tag}
	مستوى الكلان : {level}
	عدد الاعضاء :{mem}
	وصف الكلان :{description}
	سلسلة الحروب المتتالية تم فوز بها:{winst} 
	عدد الحروب التي تم فوز بها:{win}
	عدد الحروب الي خسرها : {lost}
	**"""
	except KeyError:
		text = f"""**
		اسم الكلان : {name}
	هاشتاك : {tag}
	مستوى الكلان : {level}
	عدد الاعضاء :{mem}
	وصف الكلان :{description}
	سلسلة الحروب المتتالية تم فوز بها:{winst} 
	عدد الحروب التي تم فوز بها:{win}
	**"""
	return text
STARTKEY = InlineKeyboardMarkup(
       [
         [
           InlineKeyboardButton("≈ إذاعة للمستخدمين ≈", callback_data="broadcast")
         ],
         [
           InlineKeyboardButton("≈ الاحصائيات ≈", callback_data="stats"),
           InlineKeyboardButton("≈ الأدمنية ≈", callback_data="adminstats"),
           InlineKeyboardButton("≈ المحظورين ≈", callback_data="bannedstats"),
         ],
         [
           InlineKeyboardButton("≈ كشف مستخدم ≈",callback_data="whois"),
           InlineKeyboardButton("≈ حظر مستخدم ≈",callback_data="ban"),
         ],
         [
           InlineKeyboardButton("≈ الغاء حظر مستخدم ≈",callback_data="unban"),
         ],
         [
           InlineKeyboardButton("≈ رفع ادمن ≈",callback_data="addadmin"),
           InlineKeyboardButton("≈ تنزيل ادمن ≈",callback_data="remadmin"),
         ]
       ]
     )
Rep = InlineKeyboardMarkup(
       [
         [
           InlineKeyboardButton("Search in account", callback_data="Ha"),
           InlineKeyboardButton("Search in clans", callback_data="has"),
           ],
           [
           InlineKeyboardButton("Channel Bot",url = 'https://t.me/coc_Arab'),
           ],
           ]
          )
ST = InlineKeyboardMarkup(
       [
         [
           InlineKeyboardButton("بحث عن حساب", callback_data="Hasht"),
           InlineKeyboardButton("بحث عن كلان", callback_data="hashg"),
           ],
           [
           InlineKeyboardButton("قناة البوت",url = 'https://t.me/coc_Arab'),
           ],
           ]
          )
Ne = InlineKeyboardMarkup(
       [
         [
           InlineKeyboardButton("عربي", callback_data="Ar"),
           InlineKeyboardButton("English", callback_data="en"),
           ],
           ]
          )
if not botdb.get("db"+token.split(":")[0]):
   data = {
     "users":[],
     "admins":[],
     "banned":[],
   }
   botdb.set("db"+token.split(":")[0], data)

if not ownerID in botdb.get("db"+token.split(":")[0])["admins"]:
   data = botdb.get("db"+token.split(":")[0])
   data["admins"].append(ownerID)
   botdb.set("db"+token.split(":")[0], data)

@bot.on_message(filters.command("start") & filters.private)
async def on_start(c,m):
   getDB = botdb.get("db"+token.split(":")[0])
   if m.from_user.id in getDB["banned"]:
     return await m.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   if m.from_user.id == ownerID or m.from_user.id in getDB["admins"]:
     await m.reply(f"**• أهلاً بك ⌯ {m.from_user.mention}\n• إليك لوحة تحكم الادمن**",reply_markup=STARTKEY,quote=True)
   if not m.from_user.id in getDB["users"]:
      data = getDB
      data["users"].append(m.from_user.id)
      botdb.set("db"+token.split(":")[0], data)
      allm = len(getDB['users'])
      for admin in data["admins"]:
         text = f"– New user stats the bot :"
         username = "@"+m.from_user.username if m.from_user.username else "None"
         text += f"\n\n𖡋 𝐔𝐒𝐄 ⌯  {username}"
         text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {m.from_user.mention}"
         text += f"\n𖡋 𝐈𝐃 ⌯  `{m.from_user.id}`"
         text += f"\n𖡋 𝐃𝐀𝐓𝐄 ⌯  **{date.today()}**"
         text += f"\n𖡋𝐌𝐄𝐌𝐁𝐄𝐑 𝐀𝐋𝐋 ⌯ {allm}"
         try: await c.send_message(admin, text, reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (m.from_user.first_name,user_id=m.from_user.id)]]))
         except: pass
   data = {"name":m.from_user.first_name[:25], "username":m.from_user.username, "mention":m.from_user.mention(m.from_user.first_name[:25]),"id":m.from_user.id}
   botdb.set(f"USER:{m.from_user.id}",data)


@bot.on_message(filters.private & ~filters.service)
async def on_messages(c,m):       
   if botdb.get(f"broad:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      text = "**— جاري إرسال الإذاعة إلى المستخدمين**\n"
      reply = await m.reply(text,quote=True)
      count=0
      users=botdb.get("db"+token.split(":")[0])["users"]
      for user in users:
        try:
          await m.copy(user)
          count+=1
          await reply.edit(text+f"**— تم ارسال الإذاعة الى [ {count}/{len(users)} ] مستخدم**")
        except FloodWait as x:
          await asyncio.sleep(x.value)
        except Exception:
          pass
      return True
   
   if m.text and botdb.get(f"whois:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
         name=getUser["name"]
         id=getUser["id"]
         mention=getUser["mention"]
         username="@"+getUser["username"] if getUser["username"] else "None"
         language=botdb.get(f"LANG:{id}")
         text = f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
         text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
         text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
         text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
         text += f"\n𖡋 𝐀𝐂𝐂 𝑳𝐈𝐍𝐊 ⌯  **{mention}**"
         return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"ban:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك حظر ⌯ {getUser['mention']} ⌯ لأنه ادمن",quote=True)
        else:
          if getUser["id"] in botdb.get("db"+token.split(":")[0])["banned"]:
            return await m.reply(f"– لا يمكنك حظر ⌯ {getUser['mention']} ⌯ لأنه محظور مسبقاً",quote=True)
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user added to blacklist:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["banned"].append(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"unban:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك الغاء حظر ⌯ {getUser['mention']} ⌯ لأنه ادمن",quote=True)
        else:
          if not getUser["id"] in botdb.get("db"+token.split(":")[0])["banned"]:
            return await m.reply(f"– لا يمكنك الغاء حظر ⌯ {getUser['mention']} ⌯ لأنه غير محظور مسبقاً",quote=True)
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user deleted from blacklist:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["banned"].remove(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"add:{m.from_user.id}") and m.from_user.id == ownerID:
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك رفع ⌯ {getUser['mention']} ⌯ لأنه ادمن مسبقاً",quote=True)
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["banned"]:
          return await m.reply(f"– لا يمكنك رفع ⌯ {getUser['mention']} ⌯ لأنه محظور",quote=True)
        else:          
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user added to admins list:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["admins"].append(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"rem:{m.from_user.id}") and m.from_user.id == ownerID:
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if not getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك تنزيل ⌯ {getUser['mention']} ⌯ لأنه مو ادمن",quote=True)
        if getUser["id"] == ownerID:
          return await m.reply(f"– لا يمكنك تنزيل ⌯ {getUser['mention']} ⌯ لأنه مالك البوت",quote=True)
        else:
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user deleted from admins list:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["admins"].remove(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)

@bot.on_callback_query()
async def on_Callback(c,m):      
   if m.data == "broadcast" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• أرسل الإذاعة الآن ( صورة ، نص ، ملصق ، ملف ، صوت )\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"broad:{m.from_user.id}",True)
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      
   if m.data == "whois" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• ارسل الآن ايدي المستخدم للكشف عنه\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"whois:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      
   if m.data == "ban" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لحظره\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"ban:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
   
   if m.data == "unban" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لرفع حظره\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"unban:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
   
   if m.data == "addadmin" and m.from_user.id == ownerID:
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لرفعه ادمن\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"add:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
   
   if m.data == "remadmin" and m.from_user.id == ownerID:
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لرفعه ادمن\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"rem:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")

   if m.data == "back" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      #await m.answer("• تم الرجوع بنجاح والغاء كل شي ",show_alert=True)
      await m.edit_message_text(f"**• أهلاً بك ⌯ {m.from_user.mention}\n• إليك لوحة تحكم الادمن**",reply_markup=STARTKEY)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      
   if m.data == "stats" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      users = len(botdb.get("db"+token.split(":")[0])["users"])
      await m.answer(f"• احصائيات البوت ⌯ {users}", show_alert=True,cache_time=10)
      
   if m.data == "adminstats" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      admins = len(botdb.get("db"+token.split(":")[0])["admins"])
      await m.answer(f"• احصائيات الادمنية ⌯ {admins}\n• سيتم ارسال بيانات كل آدمن", show_alert=True,cache_time=60)
      text = "- الادمنية:\n\n"
      count = 1
      for admin in botdb.get("db"+token.split(":")[0])["admins"]:
         if count==101: break
         getUser = botdb.get(f"USER:{admin}")
         mention=getUser["mention"]
         id=getUser["id"]
         text += f"{count}) {mention} ~ (`{id}`)\n"
         count+=1
      text+="\n\n—"
      await m.message.reply(text,quote=True)
   
   if m.data == "bannedstats" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      bans = botdb.get("db"+token.split(":")[0])["banned"]
      if not bans:  return await m.answer("• لا يوجد محظورين", show_alert=True,cache_time=60)
      await m.answer(f"• احصائيات المحظورين ⌯ {len(bans)}\n• سيتم ارسال بيانات كل المحظورين", show_alert=True,cache_time=60)
      text = "- المحظورين:\n\n"
      count = 1
      for banned in bans:
         if count==101: break
         getUser = botdb.get(f"USER:{banned}")
         mention=getUser["mention"]
         id=getUser["id"]
         text += f"{count}) {mention} ~ (`{id}`)\n"
         count+=1
      text+="\n\n—"
      await m.message.reply(text,quote=True)
   if m.data == 'hashg':
   	getDB = botdb.get("db"+token.split(":")[0])
   	if m.from_user.id in getDB["banned"]:
   		return await m.message.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   	else:
	   	assk = await c.ask(m.message.chat.id,"• ارسل الآن ايدي الكلان الذي تريد اضهار المعلومات",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
	   	try:
		   	idd = assk.text.replace('#','')
		   	cla = await ns(idd)
		   	await m.message.reply(cla,quote=True,reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
	   	except:
	   		await m.message.reply('الايدي خطا اعد المحاوله',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
   if m.data == 'Hasht':
   	getDB = botdb.get("db"+token.split(":")[0])
   	if m.from_user.id in getDB["banned"]:
   		return await m.message.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   	else:
   		assk = await c.ask(m.message.chat.id,"• ارسل الآن ايدي الحساب الذي تريد اضهار المعلومات",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
	   	try:
	   		idgd = assk.text.replace('#','')
		   	cla = await Clash(idgd)
		   	await m.message.reply(cla,quote=True,reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
	   	except:
	   		await m.message.reply('الايدي خطا اعد المحاوله',quote=True,reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
   if m.data == 'baack':
   	await m.edit_message_text(f"**• أهلاً بك ⌯ {m.from_user.mention}\n• اختر من الانلاين الذي تحت**",reply_markup=ST)
   if m.data == 'Ar':
   	await m.edit_message_text(f"**• أهلاً بك ⌯ {m.from_user.mention}\n• اختر من الانلاين الذي تحت**",reply_markup=ST)
   if m.data == 'en':
   	await m.edit_message_text(f"**• Welcome ⌯ {m.from_user.mention}\n• Choose from the button below**",reply_markup=Rep)
   if m.data == 'bacck':
   	await m.edit_message_text(f"**• Welcome ⌯ {m.from_user.mention}\n• Choose from the button below**",reply_markup=Rep)
   if m.data == 'has':
   	getDB = botdb.get("db"+token.split(":")[0])
   	if m.from_user.id in getDB["banned"]:
   		return await m.message.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   	else:
   		assk = await c.ask(m.message.chat.id,"• Send the hashtag of the clan you want to search for",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="bacck")]]))
   		try:
	   		idgd = assk.text.replace('#','')
		   	cla = await clans(idgd)
		   	await m.message.reply(cla,quote=True,reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="baack")]]))
   		except:
	   		await m.message.reply('Wrong id, try again',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="bacck")]]))
   if m.data == 'Ha':
   	getDB = botdb.get("db"+token.split(":")[0])
   	if m.from_user.id in getDB["banned"]:
   		return await m.message.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   	else:
   		assk = await c.ask(m.message.chat.id,"• Send the hashtag of the account you want to search for",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="bacck")]]))
   		try:
		   	idd = assk.text.replace('#','')
		   	cla = await english(idd)
		   	await m.message.reply(cla,quote=True,reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("Back",callback_data="bacck")]]))
   		except:
	   		await m.message.reply('Wrong id, try again',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="bacck")]]))
@app.on_message(filters.command("start") & filters.private)
async def start_msg(app,message):
   getDB = botdb.get("db"+token.split(":")[0])
   if message.from_user.id in getDB["banned"]:
     return await message.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   else:
   	await message.reply('**Welcome to the bot. Choose English if you are a foreigner\n\nمرحبا بك في البوت اختر اللغة العربية **',reply_markup=Ne,quote=True)
bot.start()
app.start()
print("ur bot started successfully")
idle()