import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA3NzU2Mzg1NjAzMDgxMDE0Mw.G2BJkf.393BRSTL2y8UcAeX8zid9N-3-d0i9FpEiFFVQ0'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} od teraz działa'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} powiedział: '{user_message}' '({channel})'")

        if user_message[0] == '&':
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)
        print(user_message)

    client.run(TOKEN)
