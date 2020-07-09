import json
from collections import Counter


with open('./swit_chat.json', 'r') as f:

    json_data = json.load(f)

py_data = json.dumps(json_data)

lst = []

for i in json_data['data'] :
	lst.append(i['user_name'])


result = Counter(lst)

max = 0
check = ""

for key in result :
	if result[key] > max :
		max = result[key]
		check = key

print("=============둑근둑근 투머치 토커 찾기============")
print(f"하하하하하 투머치 토커는 {max}번 채팅하신 {check}님입니다!")
