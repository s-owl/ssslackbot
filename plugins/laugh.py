from slackbot.bot import listen_to


@listen_to('ㅋㅋㅋ')
def bot(message):
    message.reply(message+'ㅋㅋ')
