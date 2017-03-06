from slackbot.bot import listen_to


@listen_to('(ㅋ*)$')
def laugh(message, arg):
    k = arg.count('ㅋ')
    if k > 1:
        message.send('ㅋ'*(k+2))


@listen_to(':parrot:')
def parrot(message):
    message.send(':parrot:')
