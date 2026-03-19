import json


info = '''{
    "name":"이정호",
    "addr":"노량진",
    "foods":["맥주","베이컨"]
}'''

result = json.loads(info)

print("종료됨")