from dis import disco
import os
import glob
from pydoc import describe
import re
import shutil
import discord


def lcs(X, Y):

    # Refer GFG

    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


def makePath(listOfPaths, getFile=True):
    toReturn = ''
    lisToUse = listOfPaths
    if (getFile == True):
        lisToUse = listOfPaths[:-1]

    for dir in lisToUse:
        toReturn = toReturn + '/' + dir
    return toReturn+'/'


def getDir(currentPath):

    # for currentPath use this format for input -> folder1/folder2/
    # example input: Buildings/Village/

    currentPath = '.'+currentPath

    listdir = os.listdir(currentPath)
    listToReturn = []

    for obj in listdir:
        if (os.path.isdir((currentPath+obj))):
            listToReturn.append(obj)

    if (len(listToReturn)):
        return listToReturn

    return None


def getObecjt(path, obj):

    # for path use this format for input -> folder1/folder2/
    # for obj use this format for input -> name_of_object

    # example input: (Buildings/Village/, pub)

    # check for info file

    try:
        objPath = '.'+path+obj
        listOfPNG = os.listdir(objPath+'/.')
    except:
        objPath = '.'+path
        listOfPNG = os.listdir(objPath+'/.')

    bestMatchLength = -100
    bestMatchFile = None
    copied = False

    for file in listOfPNG:
        lcsValue = lcs(file, (obj+'.png'))
        lcsValue = lcsValue - abs(len(file)-len((obj+'.png')))

        if (lcsValue > bestMatchLength):
            bestMatchLength = lcsValue
            bestMatchFile = file

    if (bestMatchFile != None):
        shutil.copyfile(objPath+'/'+bestMatchFile, "output.png")
        copied = True

    if (os.path.exists((objPath+'/info.txt'))):
        with open((objPath+'/info.txt'), 'r') as file:
            data = file.read()
            data = data.split('\n')
            return (data, copied)
    elif (os.path.exists((objPath+'/Info.txt'))):
        with open((objPath+'/Info.txt'), 'r') as file:
            data = file.read()
            data = data.split('\n')
            return (data, copied)
    return (None, copied)


def get_list_files(path):

    container = list()
    for x in os.listdir(path):
        if os.path.splitext(x)[1] != ".txt":
            container.append(os.path.splitext(x)[0])
    return container


commands_dict = {"ammunition": "Information on ammunition", "attachments": "Information on attachments",
                 "buildings": "Information on buildings", "clothes": "Information on clothes", "loot": "Information on loot",
                 "magazines": "Information on magazines", "tools": "Information on tools", "vehicles": "Information on vehicles",
                 "weapons": "Information on weapons", "emojis": "Get relevant files for the emojis"}

help_embed = discord.Embed(title="DayzKillFeed",
                           description="**Help Menu:**", color=discord.Color.from_rgb(147, 15, 247))
help_embed.set_thumbnail(
    url="https://media1.giphy.com/media/4jmyXA9g3u0Wj2mY1H/giphy.gif")
help_embed.add_field(name="How to use this bot:",
                     value="Use the prefix before any commands: #", inline=False)
help_embed.set_image(url="https://i.imgur.com/NXVkydS.jpeg")
for c in commands_dict:
    help_embed.add_field(name=c, value=commands_dict[c], inline=False)

error_embed = discord.Embed(
    description="**Image not found !**", color=discord.Color.red())
