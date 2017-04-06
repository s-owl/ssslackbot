from slackbot.bot import listen_to


@listen_to('^((?!！)(.*[\u4e00-\u9fff]+))')
def chinese(message, *arg):
    message.send('중국어야!')
