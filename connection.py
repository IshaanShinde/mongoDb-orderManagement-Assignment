# library imports
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

# url with pass
url = "mongodb+srv://ishaanshinde08:qwe@initsample.h51oq.mongodb.net/"

# establishing connection
client = MongoClient(url, server_api = ServerApi('1'))

try:
    client.admin.command('ping')

    print("\ndeployment pinged.\nConnected to mongoDb")

except Exception as error:

    print(error)
