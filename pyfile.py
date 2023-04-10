import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://hari:<password>@cluster0.xw0uwcb.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test_db"]
collection = db["test_table"]

post1 = {"_id":3,"name":"raghul","score":9}
post2 = {"_id":4,"name":"vickeee","score":10}

# results = collection.insert_one(post2)
# collection.insert_many([post1, post2])

# results = collection.find({"name":"abi"})
# results = collection.find_one({"name":"abi"})

# print(results)

# results = collection.find({})

# results = collection.delete_one({"_id":4})
# results = collection.delete_many({})

# results = collection.update_one( {"_id":5}, {"$set" : {"name" :"karthi"}})
# results = collection.update_many( {"_id":5}, {"$inc" : {"hello":5} } )

# results = collection.find({})

# print(results)
# for result in results:
#     print(result)

post_count = collection.count_documents({})
print(post_count)