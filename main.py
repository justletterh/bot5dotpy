from discord.ext import commands
import discord

class MyCog(commands.Cog):
  @commands.command()
  async def help(self, ctx):
    hid = 666317117154525185
    if ctx.message.content != '&&help jsk':
      msgcont = ctx.message.content[5:len(ctx.message.content)]
      await ctx.message.channel.send(content="im sorry, there is no help ***yet***...")
    if ctx.message.content == '&&help jsk' and ctx.message.author.id != hid:
      await ctx.message.channel.send(content=f"only <@!{hid}> can do that!")
    if ctx.message.content == '&&help jsk' and ctx.message.author.id == hid:
      await ctx.send("""```
The Jishaku debug and diagnostic commands.

This command on its own gives a status brief.
All other functionality is within its subcommands.

Commands:
  cancel     Cancels a task with the given index.
  cat        Read out a file, using syntax highlighting if detected.
  curl       Download and display a text file from the internet.
  debug      Run a command timing execution and catching exceptions.
  git        Shortcut for 'jsk sh git'. Invokes the system shell.
  hide       Hides Jishaku from the help command.
  in         Run a command as if it were run in a different channel.
  load       Loads or reloads the given extension names.
  py         Direct evaluation of Python code.
  py_inspect Evaluation of Python code with inspect information.
  repeat     Runs a command multiple times in a row.
  retain     Turn variable retention for REPL on or off.
  shell      Executes statements in the system shell.
  show       Shows Jishaku in the help command.
  shutdown   Logs this bot out.
  source     Displays the source code for a command.
  su         Run a command as someone else.
  sudo       Run a command bypassing all checks and cooldowns.
  tasks      Shows the currently running jishaku tasks.
  unload     Unloads the given extension names.
  voice      Voice-related commands.
```""")

def setup(bot):
  bot.add_cog(MyCog())
