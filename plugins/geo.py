from slackbot.bot import listen_to
import requests


@listen_to('!위치 (.*)')
def geo(message, address):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', {'address': address})
    loc = r.json()['results'][0]['geometry']['location']
    message.send(str(loc))
