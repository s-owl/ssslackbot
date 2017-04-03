from slackbot.bot import listen_to
from slackbot.bot import respond_to


@respond_to('(ㅋ*)$')
@listen_to('(ㅋ*)$')
def laugh(message, arg):
    k = arg.count('ㅋ')
    if k > 5:
        message.send('ㅋ'*(k+2))


@respond_to(':parrot:')
@listen_to(':parrot:')
def parrot(message):
    message.send(':parrot:')
