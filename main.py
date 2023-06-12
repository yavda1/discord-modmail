import random
import os
import sqlite3
import nextcord
from nextcord.ext import commands, application_checks, tasks
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord import Intents
import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands
connection = sqlite3.connect("db.db")
cursor = connection.cursor()

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
GuildID = "your guild id here (no quotes just as an integer)"

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
isempty = []
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if not msg.guild:
        target = msg.author.id
        ignoreCheck = cursor.execute(
            "SELECT ignored FROM ignore WHERE userId = ?",
            (target,),
        ).fetchall()
        
    
        if ignoreCheck == isempty:

            await msg.add_reaction("✅")
            channel = bot.get_channel("your channel Id here (as an integer)")

            modmailEmbed = nextcord.Embed(
                title="Mod Mail",
                description=
                msg.content,
                color=nextcord.Color.teal()
            )

            modmailEmbed.set_author(name=msg.author, icon_url=msg.author.avatar.url)
            await channel.send(embed=modmailEmbed)
        else:
            pass
    if msg.content.startswith('$hello'):
        await msg.channel.send('Hello!')
@application_checks.has_permissions(manage_messages=True)
@bot.slash_command(name="message", description="Messages to a user via modmail", guild_ids=[GuildID])
async def message(interaction: Interaction, content:str, user:nextcord.Member):
    userEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            content,
            color=nextcord.Color.green()
    )
    doneEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            f"Sent the modmail to {user} successfully",
            color=nextcord.Color.green()
    )
    errEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            f"Could not modmail {user}.",
            color=nextcord.Color.red()
    )
    userEmbed.set_author(name="Mod Team", icon_url=interaction.guild.icon.url)

    try:
        await user.send(embed=userEmbed)
        await interaction.send(embed=doneEmbed)
    except Exception as e:
        await interaction.send(embed=errEmbed)
@application_checks.has_permissions(manage_messages=True)
@bot.slash_command(name="ignore", description="Ignore users", guild_ids=[GuildID])
async def ignore(interaction: Interaction, user:nextcord.Member):
    userEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            "You are being ignored by Mod Mail",
            color=nextcord.Color.red()
    )
    doneEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            f"Ignored {user} successfully",
            color=nextcord.Color.green()
    )

    userEmbed.set_author(name="Mod Team", icon_url=interaction.guild.icon.url)
    cursor.execute(f"INSERT INTO ignore VALUES ({user.id}, '1')")
    connection.commit()
    await user.send(embed=userEmbed)
    await interaction.send(embed=doneEmbed)
@application_checks.has_permissions(manage_messages=True)
@bot.slash_command(name="unignore", description="unignore users", guild_ids=[GuildID])
async def unignore(interaction: Interaction, user:nextcord.Member):
    userEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            "You've been unignored by Mod Mail",
            color=nextcord.Color.red()
    )
    doneEmbed = nextcord.Embed(
            title="Mod Mail",
            description=
            f"Unignored {user} successfully",
            color=nextcord.Color.green()
    )

    userEmbed.set_author(name="Mod Team", icon_url=interaction.guild.icon.url)
    unignore = 0
    cursor.execute(
        "DELETE FROM ignore WHERE userId = ?",
        (user.id,)
    )
    connection.commit()
    await user.send(embed=userEmbed)
    await interaction.send(embed=doneEmbed)

    
bot.run(TOKEN)