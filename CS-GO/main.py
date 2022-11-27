
from discord.ext import commands
import discord
from discord_components import DiscordComponents, Select, SelectOption
from parse_folders import get_chunks
from processor import getObecjt, getDir, makePath, get_list_files, help_embed, error_embed, commands_dict
import asyncio
from webserver import keep_alive

bot = commands.Bot(command_prefix="#")
bot.remove_command("help")
DiscordComponents(bot)

global buildingDict
buildingDict = {}
ammunitionDict = {}
attachmentsDict = {}
clothesDict = {}
lootDict = {}
toolsDict = {}
magazinesDict = {}
vehiclesDict = {}
weaponsDict = {}
emojiDict = {}


lock = asyncio.Lock()


@bot.event
async def on_ready():
    print("The bot is live!!")


async def processInteraction():
    while True:
        interactionData = await bot.wait_for("select_option")

        await buildingsGlobal(interactionData)
        await ammunitionGlobal(interactionData)
        await attachmentsGlobal(interactionData)
        await clothesGlobal(interactionData)
        await lootGlobal(interactionData)
        await magazinesGlobal(interactionData)
        await toolsGlobal(interactionData)
        await vehiclesGlobal(interactionData)
        await weaponsGlobal(interactionData)
        await emojiGlobal(interactionData)


async def buildingsGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global buildingDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in buildingDict.keys():
            lock.release()
            return
        path = buildingDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in buildingDict.keys():
                            buildingDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in buildingDict.keys():
                buildingDict[id] = path
    lock.release()


async def ammunitionGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global ammunitionDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in ammunitionDict.keys():
            lock.release()
            return
        path = ammunitionDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in ammunitionDict.keys():
                            ammunitionDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in ammunitionDict.keys():
                ammunitionDict[id] = path
    lock.release()


async def attachmentsGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global attachmentsDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in attachmentsDict.keys():
            lock.release()
            return
        path = attachmentsDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in attachmentsDict.keys():
                            attachmentsDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in attachmentsDict.keys():
                attachmentsDict[id] = path
    lock.release()


async def clothesGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global clothesDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in clothesDict.keys():
            lock.release()
            return
        path = clothesDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in clothesDict.keys():
                            clothesDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in clothesDict.keys():
                clothesDict[id] = path
    lock.release()


async def lootGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global lootDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in lootDict.keys():
            lock.release()
            return
        path = lootDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in lootDict.keys():
                            lootDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in lootDict.keys():
                lootDict[id] = path
    lock.release()


async def magazinesGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global magazinesDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in magazinesDict.keys():
            lock.release()
            return
        path = magazinesDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in magazinesDict.keys():
                            magazinesDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in magazinesDict.keys():
                magazinesDict[id] = path
    lock.release()


async def toolsGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global toolsDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in toolsDict.keys():
            lock.release()
            return
        path = toolsDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in toolsDict.keys():
                            toolsDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in toolsDict.keys():
                toolsDict[id] = path
    lock.release()


async def vehiclesGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global vehiclesDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in vehiclesDict.keys():
            lock.release()
            return
        path = vehiclesDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in vehiclesDict.keys():
                            vehiclesDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in vehiclesDict.keys():
                vehiclesDict[id] = path
    lock.release()


async def weaponsGlobal(interaction=None, ctx=None):

    await lock.acquire()
    global weaponsDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]
    else:
        if interaction.component.custom_id not in weaponsDict.keys():
            lock.release()
            return
        path = weaponsDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    inputToDir = makePath(path, getFile=False)

    try:
        val = getDir(inputToDir)
    except:
        val = None

    # check if my interaction

    if val:
        try:
            dropDownData = get_chunks(
                getDir(inputToDir), placeholder=f"What {path[-1]} do you need help with ?")
            await interaction.send(
                components=dropDownData)
        except:
            pass

    elif val == None:
        file_names = None
        try:
            file_names = get_list_files('.'+inputToDir)
        except:
            pass

        if file_names:
            if len(file_names) > 1:
                try:
                    dropDownData = get_chunks(
                        file_names, placeholder=f"What {path[-1]} do you need help with ?")
                    await interaction.send(components=dropDownData)

                    for option in dropDownData:
                        option = option.to_dict()
                        id = option['components'][0]['custom_id']
                        if id not in weaponsDict.keys():
                            weaponsDict[id] = path

                except:
                    pass

                lock.release()
                return

        pathToDir = makePath(path)
        response = getObecjt(pathToDir, path[-1])

        if response[0] != None:
            desc = "\n".join(response[0])
            e = discord.Embed(description=desc,
                              color=discord.Color.from_rgb(147, 15, 247))
        else:
            e = discord.Embed(color=discord.Color.from_rgb(147, 15, 247))
        if response[1]:
            file = discord.File("output.png")
            e.set_image(url="attachment://output.png")
            await interaction.send(file=file, embed=e)
        elif not response[1]:
            await interaction.send(embed=error_embed)

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in weaponsDict.keys():
                weaponsDict[id] = path
    lock.release()


async def emojiGlobal(interaction=None, ctx=None):

    files = {"Food & Drink": "Food20and20Drinks20120EMojis.zip",
             "Gamer-Geek": "Gamer-geek20EMojis.zip",
             "Ghilie": "Ghillie20Emojis.zip",
             "Jackets": "Jackets20Emojis.zip",
             "Medical": "Medical20Emojis.zip",
             "NBC": "NBC20Set20Emojis.zip",
             "Gamer-Neon": "Neon-Gamer20EMojis.zip",
             "Shoes": "Shoes20Emojis.zip",
             "Trousers": "Trousers20Emojis.zip",
             "Vets": "Vests20Emojis.zip"}

    await lock.acquire()
    global emojiDict

    dropDownData = None
    if (ctx != None):
        interaction = ctx
        path = [ctx.message.content[1:]]

    else:
        if interaction.component.custom_id not in emojiDict.keys():
            lock.release()
            return
        path = emojiDict[interaction.component.custom_id].copy()
        path.append(interaction.values[0])

    if len(path) == 1:
        pass
        dropDownData = get_chunks(
            list(files.keys()), placeholder="What Emojis do you need help with ?")

        await interaction.send(
            components=dropDownData)

    else:

        await interaction.send(file=discord.File("/home/runner/ChillyCyberEmulators/"+path[0]+"/"+files[interaction.values[0]]))

    if dropDownData != None:
        for option in dropDownData:
            option = option.to_dict()
            id = option['components'][0]['custom_id']
            if id not in emojiDict.keys():
                emojiDict[id] = path

    lock.release()


@bot.command()
async def buildings(ctx):
    await ctx.send(embed=help_embed)
    await buildingsGlobal(ctx=ctx)


@bot.command()
async def ammunition(ctx):
    await ctx.send(embed=help_embed)
    await ammunitionGlobal(ctx=ctx)


@bot.command()
async def attachments(ctx):
    await ctx.send(embed=help_embed)
    await attachmentsGlobal(ctx=ctx)


@bot.command()
async def clothes(ctx):
    await ctx.send(embed=help_embed)
    await clothesGlobal(ctx=ctx)


@bot.command()
async def loot(ctx):
    await ctx.send(embed=help_embed)
    await lootGlobal(ctx=ctx)


@bot.command()
async def magazines(ctx):
    await ctx.send(embed=help_embed)
    await magazinesGlobal(ctx=ctx)


@bot.command()
async def tools(ctx):
    await ctx.send(embed=help_embed)
    await toolsGlobal(ctx=ctx)


@bot.command()
async def weapons(ctx):
    await ctx.send(embed=help_embed)
    await weaponsGlobal(ctx=ctx)


@bot.command()
async def vehicles(ctx):
    await ctx.send(embed=help_embed)
    await vehiclesGlobal(ctx=ctx)


@bot.command()
async def help(ctx):
    await ctx.send(embed=help_embed)


@bot.command()
async def emojis(ctx):
    await ctx.send(embed=help_embed)
    await emojiGlobal(ctx=ctx)


@bot.command()
async def Discord(ctx):
    await ctx.send("http://discord.gg/SnNzeTx")


@bot.command()
async def dashboard(ctx):
    await ctx.send("http://dayzkillfeed.gg/")


keep_alive()
loop = asyncio.get_event_loop()
loop.create_task(processInteraction())
loop.create_task(
    bot.run("YOUR_BOT_TOKEN"))
loop.run_forever()
