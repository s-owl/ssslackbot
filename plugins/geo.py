from slackbot.bot import listen_to
from slackbot.bot import respond_to
import requests


@respond_to('위치 (.*)')
@listen_to('!위치 (.*)')
def geo(message, address):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', {'address': address})
    loc = r.json()['results'][0]['geometry']['location']
    message.send(str(loc))
