import requests
import ambient
import threading
import json
import data_csv

AMBIENT_CHANNEL_ID_PUBLIC ="91488"
AMBIENT_READ_KEY_PUBLIC = "ec1c09455dc8fd8d"
AMBIENT_CHANNEL_ID_TEST = "92194"             # 家庭土
AMBIENT_READ_KEY_TEST = "be75dfc419277287"


# amb = ambient.Ambient(AMBIENT_CHANNEL_ID_TEST, '' , AMBIENT_READ_KEY_TEST)
# amb = ambient.Ambient(AMBIENT_CHANNEL_ID_PUBLIC, '',AMBIENT_READ_KEY_PUBLIC)

# d = amb.read()
# print(d)

def get_ambient_data():
    stop_event = threading.Event()
    url = f"https://ambidata.io/api/v2/channels/{AMBIENT_CHANNEL_ID_TEST}/data"
    params = {"readKey": AMBIENT_READ_KEY_TEST, "n": 10}  # 最新10件を取得
    r = requests.get(url, params=params)
    print(r.status_code)  # 200 が返ればOK
    print(r.json())       # JSONデータ表示
    data_r_list = data_csv.csv_write_iterator(r)
    return data_r_list


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    data_r_list = get_ambient_data()
    print(data_r_list)
