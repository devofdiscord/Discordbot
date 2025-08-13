import discord
from discord.ext import commands

# ضع التوكن الخاص بالبوت هنا
TOKEN = "MTQwNTI0MTI0NDI5MTk1Njc2Nw.GDs8lh.Mre8OF0v65Nu1Zj_D3mYlmgz65diXqsOFpgYyU"

# تحديد البريفكس (هنا نستخدم الحروف مباشرة)
bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

# منع ظهور رسالة help الافتراضية
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"✅ تم تشغيل البوت باسم {bot.user}")

# أمر القوانين
@bot.command(name="قوانين")
async def rules(ctx):
    rules_text = """
**قوانين سيرفر عرب بلود**

1- ممنوع السب
2- ممنوع التكلم بالسياسه 
3- ممنوع انتحال رتبه اداريه
4- ممنوع طلب ادمن 
5- ممنوع تزعج الاداره و الادمن بدون سبب
7- ممنوع النشر
8- يمنع وضع صور مخله
9- يمنع التلميح لسب
10- يمنع التكلم عن المثليين أو ما شبه

وبس نتمنى منكم احترام و تقدير القوانين
"""
    await ctx.send(rules_text)

# باند = B
@bot.command(name="B")
@commands.has_permissions(ban_members=True)
async def ban_user(ctx, member: discord.Member, *, reason="No reason"):
    await member.ban(reason=reason)
    await ctx.send(f"🚫 تم حظر {member.mention} - السبب: {reason}")

# طرد = K
@bot.command(name="K")
@commands.has_permissions(kick_members=True)
async def kick_user(ctx, member: discord.Member, *, reason="No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 تم طرد {member.mention} - السبب: {reason}")

# قفل الروم = ق
@bot.command(name="ق")
@commands.has_permissions(manage_channels=True)
async def lock_channel(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔒 تم قفل الروم.")

# فتح الروم = ف
@bot.command(name="ف")
@commands.has_permissions(manage_channels=True)
async def unlock_channel(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔓 تم فتح الروم.")

# تشغيل البوت
bot.run(TOKEN)