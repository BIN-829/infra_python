from turtle import reset

import yaml

info = '''
name: 조용빈
addr: 대구시
foods:
    - 소주
    - 삼겹살
isMan: true
body:
    weight: 80
    height: 180
'''

info_dict = yaml.safe_load(info)

print(info_dict)
print(type(info_dict))

yaml_str = yaml.dump(info_dict, allow_unicode=True)

print(yaml_str)
print(type(yaml_str))



result = yaml.safe_load(info)

print(result)
#result(dict type)을 다시 yaml 형식으로 변환하기
result2=yaml.dump(result, allow_unicode=True, sort_keys=False)

print(result2)

print("종료 합니다")