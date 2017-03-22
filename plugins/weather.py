from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot_settings import DARKSKY_API
from slackbot_settings import SKHU_LOCATION
import requests
import forecastio


@respond_to('날씨 (.*)')
@listen_to('!날씨 (.*)')
def weather(message, address):

    if address is None:
        address = "성공회대학교"

    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', {'address': address})
    loc = r.json()['results'][0]['geometry']['location']

    forecast = forecastio.load_forecast(
        DARKSKY_API,
        loc['lat'],
        loc['lng'],
    )

    data = forecast.currently()
    string = "날씨 예보 입니다. " + forecast.daily().summary +\
             "\n지금" + address +\
             "의 날씨 입니다! " +\
             "\n온도: " + str(data.temperature) + '℃' +\
             "\n기상: " + data.summary +\
             "\n풍속: " + str(round(data.windSpeed, 1)) + 'm/s'
    message.send(string)
