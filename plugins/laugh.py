from slackbot.bot import listen_to


@listen_to('(ㅋ*)$')
def bot(message, arg):
    k = arg.count('ㅋ')
    if k > 1:
        message.reply('ㅋ'*(k+2))
