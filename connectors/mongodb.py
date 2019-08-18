from pymongo import MongoClient

_mongodb_login = 'melkor'
_mongodb_password = 'w%ExWvtxPrEl#rBc'

mongodb_client = MongoClient("mongodb://{}:{}@localhost:27017".format(_mongodb_login, _mongodb_password))
