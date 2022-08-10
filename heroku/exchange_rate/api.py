import requests
from pprint import pprint
from pymongo import MongoClient
from datetime import datetime


def get_rates():
    resp = {}
    url = 'https://api.exchangerate.host/latest'

    response = requests.get(url)
    data = response.json()
    resp['date'] = data['date']
    resp['base'] = data['base']   
    resp['rates'] =  data['rates']
    return resp
# get_rates()


def connect_():
    uri = "mongodb+srv://finalprojectDP:Georgian123@finalproject.zroift8.mongodb.net/test"
    client = MongoClient(uri)
    db = client.forex
    collection = db['rates']
    return collection


def upload_data():
    data = get_rates()
    collection = connect_()
    date_today = datetime.now().strftime("%Y-%m-%d")
    # resp = collection.find({"date":date_today})
    if data['date'] == date_today:
        collection.insert(data)


# upload_data()
def print_date():
    with open('romil', '+w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d-%s"))

print_date()