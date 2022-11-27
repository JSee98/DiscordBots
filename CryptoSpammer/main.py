from webserver import keep_alive
import multibot
from discord.ext import tasks
import numpy as np
import asyncio
import random

# change 
channel_id = 934475265076252713

# add new
id1 = 'OTQxNjY2MzQzMzc4MzY2NDk0.YgZRHw.h5XvmlbNn75ZRoj5S0BEGBfBHms'
id2 = 'OTQxNjk3MTk0ODQxNDg1MzMz.YgZt2w.Uh-yPgTKkLKi_KTSLmMeiVfdM1w'
id3 = 'OTQxNjk3NTIyNTk2OTc4Njg4.YgZuKQ._FJWwRqBB19aalbu1eIAS1sVSrw'
id4 = 'OTQxNjk4MTA4MzM1NzUxMTk4.YgZutA.jh9yIaXxKyds_dO_GaZNlmeq2lc'
id5 = 'OTQxNjk4Mzc5NjkwNDE4MTk2.YgZu9Q.S4q_i4FnT_oz7AUHdOg2GVggmkA'
id6 = 'OTQxNjk4NzY2Mjc1MjMxNzk1.YgZvUQ.Aw-ToiT_Ttt8bBQ5hZL6x66dbsk'

#create new
mybot1 = multibot.Bot(channel_id, id1)
mybot2 = multibot.Bot(channel_id, id2)
mybot3 = multibot.Bot(channel_id, id3)
mybot4 = multibot.Bot(channel_id, id4)
mybot5 = multibot.Bot(channel_id, id5)
mybot6 = multibot.Bot(channel_id, id6)

# update
bot_list = [mybot1, mybot2,mybot3,mybot4,mybot5,mybot6]

# check with me
start = 0
stop = 60

message_list = ["Wow!",
            "Let’s goo!",
            "LFG",
            "What a Project!",
            "This will be the moonshot!",
            "I’ve never seen so much detail!",
            "The artists did an incredible job When is the mint?",
            "I need 2! Let’s go Vikings!",
            "This will be the biggest project of 2022.",
            "who agrees with me?",
            "To the moon Let’s conquer the metaverse I’m getting shiba Viking for sure.",
            "Who’s with me?",
            "I hope I can get one.",
            "I think there’s a lot of people who will try… 🔥🔥🔥 ♥️♥️♥️",
            "Our website looks sick!",
            "This roadmap is crazy!",
            "I can’t wait to earn SHIB Let’s head to Mars!",
            "I’m loving this community!",
            "What a community, you’re all so supportive This art is sick!",
            "Wow, I’m so happy to be here so early!",
            "The roadmap looks promising!",
            "Looks like the founders are killing it!",
            "How do I get WL?",
            "I’ve seen a lot of NFT projects but this one looks promising",
            "The Shiba Vikings clan looks sick Where is everybody from?",
            "This is an easy moonshot 🤩",
            "I love the People in here Holy the design is dope This popped up on my feed, I knew I was missing out Let’s go shiba Vikings!",
            "This is the best project of 2022!",
            "The quality is amazing",
            "What’s up guys, let’s do this!",
            "Wow, all you guys in here are amazing!",
            "Let it rip baby!",
            "🪓🪓🪓🪓",
            "🙌🙌🙌",
            "🚀🚀🚀🚀",
            "⚔️⚔️⚔️",
            "Let’s go shiba Vikings clan!",
            "I really hope I can get one at mint This project will skyrocket!",
            "Shiba Viking to the top",
            "Let’s go I’m so exited to be part of this!",
            "Shiba Vikings to the moon!",
            "To Mars and beyond 🚀👍"
            ]

global shuffled_message
shuffled_message = [message for message in message_list]

global sleep_lis

num_bots = len(bot_list)

sleep = [random.randint(start,stop) for i in range(num_bots)]

np.random.shuffle(shuffled_message)

lock = asyncio.Lock()

# change to 5 minutes
@tasks.loop(minutes=5.0, reconnect=True)
async def send_message():
    global shuffled_message
    global sleep
    global start
    global stop
    sleep.sort()
    runner = 0

    for bot in bot_list:
        await lock.acquire()
        if (len(shuffled_message) > 0):
            await bot.worker.wait_until_ready()
            await bot.send_message(shuffled_message.pop())
        else:
            shuffled_message = [message for message in message_list]
            np.random.shuffle(shuffled_message)

        sleep_time = sleep[runner]
        runner+=1

        await asyncio.sleep(sleep_time)
        lock.release()
    sleep = [random.randint(start,stop) for i in range(num_bots)]

keep_alive()
loop = asyncio.get_event_loop()
send_message.start()
# repeat for other bots
loop.create_task(mybot1.start_bot())
loop.create_task(mybot2.start_bot())
loop.create_task(mybot3.start_bot())
loop.create_task(mybot4.start_bot())
loop.create_task(mybot5.start_bot())
loop.create_task(mybot6.start_bot())
loop.run_forever()

print("Started all bots")

