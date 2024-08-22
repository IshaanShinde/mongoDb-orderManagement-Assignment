# library imports
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

url = "mongodb+srv://ishaanshinde08:qwe@initsample.h51oq.mongodb.net/"

client = MongoClient(url, server_api = ServerApi('1'))

dataBase = client['orderManagement']
orderCollection = dataBase['orders']

# function to update the order
def updateOrder(orderId, productName = None, quantity = None, billAmount = None):

    query = {"_id": ObjectId(orderId)}
    newValues = {}

    # if a value is passed to the function, it adds it, otherwise it will default by None
    if productName:
        newValues["productName"] = productName
    if quantity:
        newValues["quantity"] = quantity
    if billAmount:
        newValues["billAmount"] = billAmount

    update = {"$set": newValues}

    result = orderCollection.update_one(query, update)

    # if a change is detected -> display success message
    if result.modified_count > 0:
        print(f"\norderId: {orderId} updated")
    else:
        print("\ninvalid orderId")

# function to accept the values
def accept_update_values():
    # accept the order
    orderId_toUpdate = input("\nenter the orderId: ")
    # accept new name
    productName_new = input("\nenter the new productName: ")
    # accept the quantity
    quantity_new = int(input("\nenter the new quantity: "))
    # accept the billAmount
    billAmount_new = int(input("\nenter the name of the new billAmount: "))

    return orderId_toUpdate, productName_new, quantity_new, billAmount_new

orderId_toUpdate, productName_new, quantity_new, billAmount_new = accept_update_values()

updateOrder(orderId_toUpdate, productName_new, quantity_new, billAmount_new)
