from slackbot.bot import listen_to
from yandex_translate import YandexTranslate
from slackbot_settings import YANDEX_TRANSLATE_API


translate = YandexTranslate(YANDEX_TRANSLATE_API)


@listen_to('^(?!！)(.*[\u4e00-\u9fff]+.*)')
def chinese(message, *arg):
    string = translate.translate(arg[0],'zh-ko')
    message.send(string['text'][0])
