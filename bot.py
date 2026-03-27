@bot.command()
async def spam(ctx, times: int, *, message: str):
    """Sends a message multiple times. Usage: !spam <times> <message>"""
    if times < 1:
        await ctx.send("You must send a message at least once!")
        return
    for i in range(times):
        await ctx.send(message)