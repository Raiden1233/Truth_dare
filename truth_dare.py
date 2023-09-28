# Truth and dare game implementation
import truth as t
import Dare as d

class Truth(discord.ui.View):
   def __init__(self, icon_url,name):
      super().__init__(timeout = None)
    #   self.is_persistent()
      self.icon_url = icon_url
      self.name = name
       


   @discord.ui.button(label= 'Truth',custom_id=' button1', style = discord.ButtonStyle.green)
   async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
    
    em = discord.Embed(title ='Question', description = t.truth_()) # already assigned the value to it
    em.set_author(name=f'requested by {self.name}',
                  icon_url= self.icon_url)
    
    # await interaction.response.edit_message(embed= em, view= None)
    # await interaction.followup.send(view=Truth(self.icon_url, self.name))
    await interaction.response.send_message(embed= em, delete_after=7)



   @discord.ui.button(label= 'Dare',custom_id=' button2', style = discord.ButtonStyle.red)
   async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
    
    em = discord.Embed(title ='Dare', description = d.dare()) 
    em.set_author(name=f'requested by {self.name}',
                  icon_url= self.icon_url)
    

    
    # await interaction.response.edit_message(embed= em, view= None)
    # await interaction.followup.send(view=Truth(self.icon_url, self.name))
    await interaction.response.send_message(embed= em, delete_after=10)



# Truth and dare game implementation
@Raiden.tree.command(name='truth_or_dare', description='Generic truth and dare game smh') # repelace @Raien with your client name or leave it as @bot
async def truth(ctx: discord.Interaction):

   em = discord.Embed(description = '⌦ 𓊈𒆜 𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆 𝕋ℝ𝕌𝕋ℍ 𝕆ℝ 𝔻𝔸ℝ𝔼 𒆜𓊉࿐☠️\n\n**RULES**\n** ♡˗ˏ✎ ➔ You have only 7 seconds to answer and 10 to do the dare**\n**♡˗ˏ✎ ➔ You have to answer honestly**\n** ♡˗ˏ✎ ➔You have to do the dare as well (NO CHEATING)**\n')
   em.set_author(name=f'requested by {ctx.user.name}', icon_url=ctx.user.avatar)
   em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
   
   await ctx.response.send_message(embed= em, view= Truth(ctx.user.avatar, ctx.user.name))