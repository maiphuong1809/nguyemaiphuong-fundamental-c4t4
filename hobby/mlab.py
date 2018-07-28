
import mongoengine

host = "ds253831.mlab.com"
port = 53831
db_name = "c4t4"
user_name = "alexnguyen"
password = "maiphuong18"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())