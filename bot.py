#+++++++++++++++++++++++++++++++++++++++#
#   █████████████████▀████████████████  #
#   █─▄▄▄▄█▄─▄▄─█─▄▄▄▄█▄─██─▄█▄─▀█▄─▄█  #                                                                            P.S {I'm a beginner so don't judge too harshly}
#   █▄▄▄▄─██─▄█▀█─██▄─██─██─███─█▄▀─██  #
#   ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▀  #
#+++++++++++++++++++++++++++++++++++++++#

### IT'S MY FIRST DISCORD.PY GIVEAWAY BOT ### 
### I HAVE A SLASH COMMAND VERSION TO, BUT I'M TOO LAZY TO UPLOAD IT HERE ###
#+++++++++++++++++ imports 
import random
from time import sleep
import discord as dick
from discord.ext import commands as cum

#+++++++++++++++++ i'm too lazy to create config file 
prefix = 'prefix'
token = 'token'


intents = dick.Intents.all()
intents.members = True
intents.message_content = True
slave = cum.Bot(command_prefix=cum.when_mentioned_or(prefix), intents=intents, help_command=None)

#+++++++++++++++++ ButtomView class for reroll button 
class ButtonView(dick.ui.View):
    def __init__(self):
        super().__init__()
    @dick.ui.button(label="Reroll", 
                    style=dick.ButtonStyle.gray, 
                    emoji='▫️') #It's reroll button create :)
    async def function_name(self, 
                            i: dick.Interaction, 
                            button: dick.ui.Button):
        # It's code for reroll winner. You can do it infinity times
        while True:
            winner = roll(guildf.members)
            if winner.bot != True:
                break
            else:
                winner = roll(guildf.members)
        
        # Embed with new winner
        m = dick.Embed(title="Reroll!", description=f"\n **<:discotoolsxyzicon11:1103282990223732796> New winner: <@{winner.id}> | {winner}**\n\n** <:discotoolsxyzicon19:1103290455355043883> Оrganizer: {roll_author}**", color=dick.Color.light_grey())
        m.set_thumbnail(url='https://cdn.discordapp.com/attachments/1059438957068296226/1103288664475320520/giveaway-logo_848869-2-PhotoRoom.png-PhotoRoom_1.png')
        await i.response.send_message(embed=m, view=ButtonView())



@slave.event # on_ready event 
async def on_ready():
    print(f"-------------------------------\nLogged in as {slave.user}")
    await slave.change_presence(status=dick.Status.online, activity=dick.Game("Seg._.n#8093 is cool"))

@slave.command()
async def fuf(ctx, 
              time_to_wait: int, 
              *, 
              prize: str):
    """Giveaway command :3""" # Dont think why it's named "fuf"
    
    
    embed = dick.Embed(title=f'New giveaway!',description=f'** <:discotoolsxyzicon19:1103290455355043883> Organizer: {ctx.message.author}**\n\n** <:discotoolsxyzicon20:1103291062283419689> Time to completion: {time_to_wait}s**\n\n** <:discotoolsxyzicon15:1103283638004629695> Prize: {prize}**', color=dick.Color.light_grey())
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1059438957068296226/1103288664475320520/giveaway-logo_848869-2-PhotoRoom.png-PhotoRoom_1.png')
    await ctx.send(embed=embed)

    # It's global variable needed for button response
    global roll_author
    roll_author = ctx.message.author
    
    await ctx.message.delete() # Deleting the message with command cuz it so ugly
    # Zzzzzzzzzzz...
    sleep(time_to_wait)

    # It's needed for button response too
    global guildf
    guildf = ctx.message.guild
    
    # Check if the winner is a bot. If this is True cycle reroll until the winner is not a bot
    while True:
        winner = roll(guildf.members)
        if winner.bot != True:
            break
        else:
            winner = roll(guildf.members)

    mb = dick.Embed(title=f'Giveaway is over!',description=f'** <:discotoolsxyzicon19:1103290455355043883> Organizer: {ctx.message.author}**\n\n**  <:discotoolsxyzicon15:1103283638004629695> Prize: {prize}**\n\n** <:discotoolsxyzicon11:1103282990223732796> Winner: <@{winner.id}> | {winner}**', color=dick.Color.light_grey())
    mb.set_thumbnail(url='https://cdn.discordapp.com/attachments/1059438957068296226/1103288664475320520/giveaway-logo_848869-2-PhotoRoom.png-PhotoRoom_1.png')

    # Send embed and add a reroll button
    await ctx.send(embed=mb, view=ButtonView())
    await ButtonView().wait()
   
def roll(sus): # Roll def so easy :D
        return random.choice(list(sus))

slave.run(token=token) # Run our slave


# It's all! Good luck :)
