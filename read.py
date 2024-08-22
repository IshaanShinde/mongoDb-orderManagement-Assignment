# library imports
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

# url with pass
url = "mongodb+srv://ishaanshinde08:qwe@initsample.h51oq.mongodb.net/"

# establishing connection
client = MongoClient(url, server_api = ServerApi('1'))

dataBase = client['orderManagement']
orderCollection = dataBase['orders']

orders = orderCollection.find()

for order in orders:
    print(f"""
        orderId: {order['_id']}
        productName: {order['productName']}
        quantity: {order['quantity']}
        billAmount: {order['billAmount']}
    """)

