# library imports
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

# url with pass
url = "mongodb+srv://ishaanshinde08:qwe@initsample.h51oq.mongodb.net/"

# establishing connection
client = MongoClient(url, server_api = ServerApi('1'))

dataBase = client['orderManagement']
orderCollection = dataBase['orders']

# function to delete an order
def deleteOrder(orderId):
    result = orderCollection.delete_one({"_id": ObjectId(orderId)})

    if result.deleted_count > 0:
        print(f"\norderId: {orderId} deleted")
    else:
        print("\ninvalid orderId")


orderId_toDelete = input("\enter the orderId to delete: ")
deleteOrder(orderId_toDelete)
