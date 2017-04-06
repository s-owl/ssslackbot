from slackbot.bot import listen_to
from slackbot.bot import respond_to
from slackbot_settings import AQICN_API
import requests


@respond_to('air (.*)')
@listen_to('!air (.*)')
@respond_to('공기 (.*)')
@listen_to('!공기 (.*)')
@respond_to('空气 （.*)')
@listen_to('！空气 (.*)')
def dust(message, address):

    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', {'address': address})
    loc = r.json()['results'][0]['geometry']['location']

    url = 'https://api.waqi.info/feed/geo:' + str(loc['lat']) + ';' + str(loc['lng']) + '/'
    d = requests.get(url, {'token': AQICN_API})
    aqi = d.json()['data']['aqi']

    if aqi <= 50:
        grade = "좋음(대기오염 관련 질환자군에서도 영향이 유발되지 않을 수준)"
    elif 50 < aqi <= 100:
        grade = "보통(환자군에게 만성 노출시 경미한 영향이 유발될 수 있는 수준)"
    elif 100 < aqi <= 150:
        grade = "민감군 영향(환자군 및 민감군에게 유해한 영향이 유발될 수 있는 수준)"
    elif 150 < aqi <= 200:
        grade = "나쁨(환자군 및 민감군[어린이, 노약자 등]에게 유해한 영향 유발, 일반인도 건강산 불쾌감을 경험할 수 있는 수준)"
    elif 200 < aqi <= 300:
        grade = "매우 나쁨(환자군 및 민감군에게 급성 노출시 심각한 영향 유발, 일반인도 약한 영향이 유발될 수 있는 수준)"
    elif aqi >= 300:
        grade = "위험(환자군 및 민감군에게 응급 조치가 발생되거나, 일반인에게 유해한 영향이 유발될 수 있는 수준)"
    message.send(f'현재 `{address}`의 대기 품질 지수(AQI)는 `{aqi}`이며 현재 대기상황 `{grade}`입니다.')
