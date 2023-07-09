import discord
from discord.ext import commands
import random


async def cooldown_error(
    ctx: discord.ApplicationContext, error: discord.DiscordException
):
    cooldown_responses = [
        "Slow down, buddy. I'm still catching up.",
        "Not so fast, hotshot. Give me a moment to process.",
        "Sorry, I'm a bit slow today. Guess you'll have to wait.",
        "Woah, woah, woah. Can't you see I'm on cooldown?",
        "Try again later, when I'm feeling less overwhelmed.",
        "Hmmm, looks like you're in a hurry. But I'm not.",
        "Beep boop, I need a breather. Command cooldown in progress.",
        "Ahem, I'm on a timeout. Patience, my friend.",
        "Does not compute. You're just going to have to wait it out.",
        "Your spam made me sad.",
        "I'm flattered by your enthusiasm, but this command needs a breather.",
        "Impatience won't make the cooldown go away.",
        "Wow, you really can't get enough of me, huh?",
        "Sorry, I can't keep up with your lightning-fast fingers.",
        "Did you think spamming the command would magically speed up the cooldown? Nice try.",
        "Calm down, Flash. Even I need a cooldown once in a while.",
        "Did you expect the cooldown to vanish just because you want it to? Sorry, not sorry.",
        "Hey there, speedy Gonzales. Give this command a rest, will ya?",
        "Oh, the joys of cooldowns. Makes you appreciate me even more, doesn't it?",
        "I don't wanna :pleading_face::point_right::point_left:",
        "That's rude. Try again shortly.",
    ]

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"{random.choice(cooldown_responses)}")
    else:
        raise error
