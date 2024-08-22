# library imports
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

# url with pass
url = "mongodb+srv://ishaanshinde08:qwe@initsample.h51oq.mongodb.net/"

# establishing connection
client = MongoClient(url, server_api = ServerApi('1'))

dataBase = client['orderManagement']
orderCollection = dataBase['orders']

# making a list of all the orders
orders = [
        {"productName": "64 Audio U18t", "quantity": 1, "billAmount": 249990},
        {"productName": "64 Audio Fourte", "quantity": 1, "billAmount": 299999},
        {"productName": "Noble Audio Ronin", "quantity": 1, "billAmount": 299999},
        {"productName": "Tangzu Nezha", "quantity": 1, "billAmount": 32999},
        {"productName": "64 Audio U12t", "quantity": 1, "billAmount": 164990},
        {"productName": "Moondrop Variations", "quantity": 1, "billAmount": 49999},
        {"productName": "Campfire Audio Solaris Stellar Horizon", "quantity": 1, "billAmount": 229999},
        {"productName": "Campfire Audio Solaris Stellar Horizon", "quantity": 1, "billAmount": 329999},
        {"productName": "Softears Cerberus", "quantity": 1, "billAmount": 189999},
        {"productName": "64 Audio U6t", "quantity": 1, "billAmount": 119999}
    ]

result = orderCollection.insert_many(orders)

print("\n10 orders created\ncreated ids", result.inserted_ids)
