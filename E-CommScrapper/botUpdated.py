from local_parser import getLatest, get_latest_hot, getLatestTarget
import discord
from discord.ext import commands, tasks
from db import insertDB, deleteEntry, queryAll, updateEntry
from urllib.parse import urlparse
import time

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="#", intents=intents)


# clears the last n messages
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


# bans the  user


@bot.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.send("Banning: " + member.name)
    await member.ban(reason=reason)

# unbans the user


@bot.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user
        user_name, user_disc = str(user).split("#")

        if (user_name, user_disc) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send("Unbanned: " + member_name)
            return
    await ctx.send("member not found")

# kicks the user


@bot.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):

    await ctx.send("Kicking: " + member.name)
    await member.kick()

# add URL


@bot.command(aliases=['au'])
@commands.has_permissions(administrator=True)
async def addurl(ctx, message):

    channel_id = ctx.message.channel.id
    channel = bot.get_channel(channel_id)
    domain = urlparse(message).netloc
    if domain == "www.funko.com":
        try:

            data = getLatest(message)

            embed = discord.Embed(
                title=data[0], description=data[3], color=discord.Color.blue(), url=data[4])
            embed.set_thumbnail(url=data[2])
            embed.add_field(name="Price ($)", value=data[1], inline=True)
            role = discord.utils.get(ctx.guild.roles, name="Funko")

            await channel.send(f'{role.mention}')
            insertDB(str(channel_id), message, str(data[5]), domain)

        except:

            embed = discord.Embed(
                title="No Product Found!", description="Please recheck your url.", color=discord.Color.red())

    elif domain == "www.hottopic.com":
        try:

            data = get_latest_hot(message)
            embed = discord.Embed(
                title=data[0], color=discord.Color.blue(), url=data[3])
            embed.set_thumbnail(url=data[1])
            embed.add_field(name="Price", value=data[2], inline=True)
            role = discord.utils.get(ctx.guild.roles, name="Funko")
            await channel.send(f'{role.mention}')
            insertDB(str(channel_id), message, str(data[0]), domain)

        except:
            embed = discord.Embed(
                title="No Product Found!", description="Please recheck your url.", color=discord.Color.red())

    elif domain == "www.target.com":
        try:

            data = getLatestTarget(message)
            embed = discord.Embed(
                title=data[0], color=discord.Color.blue(), url=data[3])
            embed.set_thumbnail(url=data[2])
            embed.add_field(name="Price ($)", value=data[1], inline=True)
            role = discord.utils.get(ctx.guild.roles, name="Funko")
            await channel.send(f'{role.mention}')
            insertDB(str(channel_id), message, str(data[0]), domain)
        except:
            embed = discord.Embed(
                title="No Product Found!", description="Please recheck your url.", color=discord.Color.red())
    else:
        embed = discord.Embed(
            title="No Product Found!", description="Please recheck your url.", color=discord.Color.red())
    await channel.send(embed=embed)
# delete url


@bot.command(aliases=['du'])
@commands.has_permissions(administrator=True)
async def deleteurl(ctx, message):
    channel_id = ctx.message.channel.id
    channel = bot.get_channel(channel_id)
    try:
        deleteEntry(str(channel_id), message)
        embed = discord.Embed(
            title="URL Deleted!",  color=discord.Color.orange())
    except:
        embed = discord.Embed(
            title="No URL Found!", description="Please recheck your url.", color=discord.Color.red())

    await channel.send(embed=embed)

# assign custom roles


@bot.command(aliases=['ar'], pass_context=True)
@commands.has_permissions(administrator=True)
async def assignrole(ctx, message, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name=message)
    await member.add_roles(role)
    embed = discord.Embed(
        description="**"+member.name + "**" + " has been assigned " + "**" + message+"**", color=discord.Color.green())
    await ctx.send(embed=embed)


# auto assign roles to user


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Funko")
    await member.add_roles(role)

# run cron job to check latets product


@tasks.loop(seconds=300.0, reconnect=True)
async def look_for_updates():
    uids, channel_ids, urls, prod_ids, domains = queryAll()

    for (url, prod_id, uid, channel_id, domain) in zip(urls, prod_ids, uids, channel_ids, domains):

        if domain == "www.funko.com":
            data = getLatest(url)
            time.sleep(5)
            new_product_id = data[-1]
            if (str(new_product_id) != prod_id):

                updateEntry(uid, new_product_id)
                
                embed = discord.Embed(
                    title=data[0], description=data[3], color=discord.Color.blue(), url=data[4])
                embed.set_thumbnail(url=data[2])
                embed.add_field(name="Price ($)", value=data[1], inline=True)
                channel = bot.get_channel(int(channel_id))
                await channel.send(f'<@&937375788020420638>')
                await channel.send(embed=embed)

        elif domain == "www.hottopic.com":
            data = get_latest_hot(url)
            time.sleep(5)
            new_product_id = data[0]
            if (str(new_product_id) != prod_id):

                updateEntry(uid, new_product_id)
                
                embed = discord.Embed(
                    title=data[0], color=discord.Color.blue(), url=data[3])
                embed.set_thumbnail(url=data[1])
                embed.add_field(name="Price", value=data[2], inline=True)
                channel = bot.get_channel(int(channel_id))
                await channel.send(f'<@&937375788020420638>')
                await channel.send(embed=embed)
        elif domain == "www.target.com":
            data = getLatestTarget(url)
            time.sleep(5)
            new_product_id = data[0]
            if (str(new_product_id) != prod_id):
                print('Got new entry', new_product_id, prod_id)
                updateEntry(uid, new_product_id)
                embed = discord.Embed(
                    title=data[0], color=discord.Color.blue(), url=data[3])
                embed.set_thumbnail(url=data[2])
                embed.add_field(name="Price ($)", value=data[1], inline=True)
                channel = bot.get_channel(int(channel_id))
                await channel.send(f'<@&937375788020420638>')
                await channel.send(embed=embed)


@look_for_updates.before_loop
async def before_look_for_updates():
    await bot.wait_until_ready()

# ERROR HANDLING


@purge.error
@deleteurl.error
@kick.error
@ban.error
@unban.error
@assignrole.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Permission Denied.",
                              description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)

look_for_updates.start()
bot.run("OTM3Mzc0MTkwNTc3ODAzMzY0.Yfazvg.8lh4MiMcs7A9x2XAMghxMTlXbsY")
