# Need ENV : SLACKBOT_API_TOKEN, DARKSKY_API
import os

DEFAULT_REPLY = "몰라"

ERROR_TO = 'junsu'

PLUGINS = [
    'plugins.example',
    'plugins.weather',
    'plugins.reactions',
]

SKHU_LOCATION = {'lat': 37.487538, 'lng': 126.825732}

try:
    DARKSKY_API = os.environ['DARKSKY_API']
except KeyError:
    pass
