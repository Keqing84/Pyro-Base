from bot import LOG, db_uri

import pymongo

"""
{'db': 'PYTHON', 'collections': 1, 'views': 0, 'objects': 3, 
'avgObjSize': 64.33333333333333, 'dataSize': 193, 'storageSize': 36864, 
'totalFreeStorageSize': 0, 'numExtents': 0, 'indexes': 1, 'indexSize': 36864, 
'indexFreeStorageSize': 0, 'fileSize': 0, 'nsSizeMB': 0, 'ok': 1}

_id || Auto Generate By Mongo, So Set The Tg Id In It

{ "address": {"$regex": "^S"} } || all documents were the address starts with the letter S (Find Function)

{ "$set": {"tg_id": 112233445}} || Only Updates The Input Key And Value And Leaves Other Un Affected (Update Func)

[{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}] || Return Format of keys() method
"""

class MongoPy:
    def __init__(self, uri, bot="KAI84", coll="bot"):
        self.client = pymongo.mongo_client.MongoClient(uri)
        self.mdb = self.client[bot]
        self.coll = self.mdb[coll]
        self.connected = self.ping(bot)
        self._ids = list(x["_id"] for x in self.keys())
        self.total_ele = len(self._ids)


    # Checks If The Db is Connected
    def ping(self):
        try:
            self.mdb.command('ping')
            return True
        except Exception as e:
            LOG.info(str(e))
            return False


    # Return The Elements Present In The Collection in list -> Dict    
    def keys(self):
        _lis = []
        for x in mycol.find():
            _lis.append(x)
        return _lis


    # Sets Keys in the collection
    def insert_value(self, key):
        if key["_id"] in self._ids:
            self.delete_value(key["_id"])
        self.coll.insert_one(key)


    # Finds The Object in The Collection
    def find_value(self, key):
        if x := self.coll.find_one(key):
            return x


    # Replaces Values With Newer Values
    def replace_value(self, ID: int,  n_key):
        query = {"_id": ID}
        new_values = { "$set": n_key }
        self.coll.update_one(query, new_values)


    # Deletes A Object From Collection
    def delete_value(self, ID):
        my_query = { "_id": ID }
        self.coll.delete_one(my_query) 


    # Deletes The Collection
    def delete_collection(self):
        self.coll.drop() 


    # The Usage Of The DB In Bytes(8 bits)
    def usage(self):
        return self.mdb.command("dbstats")["dataSize"]


    # Restarts The DB Connection **(Experimental)**
    def restart(self):
        self.client.close()
        return MongoPy(db_uri)
        
