from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot_settings import DARKSKY_API
import requests
import forecastio


@respond_to('날씨 (.*)')
@listen_to('!날씨 (.*)')
def weather(message, address):

    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', {'address': address})
    loc = r.json()['results'][0]['geometry']['location']

    forecast = forecastio.load_forecast(
        DARKSKY_API,
        loc['lat'],
        loc['lng'],
    )

    data = forecast.currently()
    string = f"현재 `{address}`의 날씨입니다.\n" \
             f"{forecast.daily().summary}\n" \
             f"\n온도: `{str(data.temperature)}℃`\n" \
             f"\n기상: `{data.summary}`\n" \
             f"\n풍속: `{str(round(data.windSpeed, 1))}m/s`"
    message.send(string)
