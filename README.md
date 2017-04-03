# ssslackbot

성공회대학교 소모임 sss의 slack에서 사용하는 채팅봇입니다.

## Requirements

- git
- python3.6
- environment variable
  - SLACKBOT_API_TOKEN (slack에서 bot을 추가하고 해당 token을 저장합니다.)
  - DARKSKY_API (날씨 plugin을 위해서 darksky에서 api를 받습니다.)
  - AQICN_API (공기 plugin을 위해서 aqicn에에서 api를 받습니다.)

## Usage

```bash
git clone https://github.com/vaporize93/ssslackbot
cd ssslackbot
pip install -r requirements.txt
python3 run.py
```

## Deploy

```bash
docker build -t ssslackbot .
docker run --name user/ssslackbot \
           --env="SLACKBOT_API_TOKEN=<your_token>" \
           --env="DARKSKY_API=<your_token>" \
           --env="AQICN_API=<your_token>" \
           -d ssslackbot
```

## Contribution

Plugin을 작성해서 PR을 넣어주세요.
Plugin은 [slackbot](https://github.com/lins05/slackbot)에서 많은 부분을 참고할 수 있습니다.
