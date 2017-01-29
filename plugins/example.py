from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('안녕')
def hi(message):
    message.reply('안녕')
    message.react('+1')


@listen_to('봇')
@listen_to('bot')
def bot(message):
    message.reply('나 불렀니?')
