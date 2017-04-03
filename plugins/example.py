from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('안녕')
def hi(message):
    message.reply('안녕')
    message.react('+1')


@respond_to('test')
@respond_to('테스트')
def bot(message):
    message.send('나 불렀니?')
