import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds243254.mlab.com:43254/final-project-bk

host = "ds243254.mlab.com"
port = 43254
db_name = "final-project-bk"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())