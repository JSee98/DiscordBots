from discord.ext import commands


class Bot:

    def __init__(self, channel_id, token):
        self.token = token
        self.channel_id = int(channel_id)
        self.worker = commands.Bot(command_prefix="#")

        
    async def start_bot(self):
        await self.worker.start(self.token)

    async def send_message(self, message):

        channel = self.worker.get_channel(self.channel_id)
        try:
            await channel.send(message)
        except :
            pass

