import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://hari:dwaynejohnson@cluster0.xw0uwcb.mongodb.net/?retryWrites=true&w=majority")
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

# post_count = collection.count_documents({})
# print(post_count)

# dbs = cluster.list_database_names()
# # print(dbs)

# training = cluster.sample_training

# collections = training.list_collection_names()
# print(collections)

inserted_id = collection.test_table.insert_one({"_id":5,"name":"karthi","score":10}).inserted_id

print(inserted_id)


# output = collection.test_table.find({"name":"abi"})
# print(output)
# for x in output:
#     print(x)

# mongoshell commands
# show dbs
# show collections
# use test_db
# db.recipes.find()
# db.recipes.find({"name": "Tacos"})
# db.recipes.find({},{"title":1})
# db.recipes.find({"title": { $regex : /taco/i }}, {"title":1})

# db.getName()

# db.new_database_name.insertOne({})

# db.recipes.find().count();
# db.recipes.find({},{"title":1})
# db.recipes.find({},{"title":1}).limit(2)
# db.recipes.find({}, {"title":1}).sort({"title":1})
# db.recipes.find({}, {"title":1}).sort({"title":-1}).limit(2);
# db.recipes.find({}, {"title":1}).sort({"title":-1}).skip(1);
# db.recipes.find({}, {"title":1}).sort({"title":-1}).skip(2).limit(1);

# db.recipes.find({ "cook_time": { $lte : 30 }}, {"title":1})
# db.recipes.find({ "cook_time": { $lte : 30 }, "prep_time": { $lte : 10 } }, {"title":1})


# db.recipes.find({"_id": 15}, {"title":1,"prep_time":1,"cook_time":1})

# db.recipes.find( { $or :  [{ "cook_time": { $lte : 30 }, "prep_time": { $lte : 10 } }] }, {"title":1})

# db.recipes.find({"tags": "easy"},{ "title":1, "tags":1})

# db.recipes.find({"tags": { $all : ["easy", "quick"]} },{ "title":1, "tags":1})
# db.recipes.find({"tags": { $in : ["easy", "quick"]} },{ "title":1, "tags":1})

# db.recipes.find({"ingredients.name": "egg"},{ "title":1})


# # ```update methods for mongoDB```

# db.examples.updateOne({"title":"Pizza"},{ $set : { "title" : "Thin crust pizza" }})

# db.examples.updateOne({"title":"Thin crust pizza"},{ $set : { "vegan" : false }})

# db.examples.updateOne({"title":"Thin crust pizza"},{ $unset : { "vegan" : 1 }})

# db.examples.updateOne({"title":"Tacos"},{ $inc : { "likes_count": 1}})

# db.examples.updateOne({"title":"Tacos"}, { $push : { "likes" : 60 }})
# db.examples.updateOne({"title":"Tacos"}, { $pull : { "likes" : 60 }})

# db.examples.replace_one( {"_id": 5}, {"title":"Tacos new", "rating": 10})

# # ```delete document```

# db.examples.deleteOne({"title": "custard_apple"})

# db.recipes.find({}, {"title": 1}).sort({"rating_avg": -1}).limit(4)

# db.recipes.find({"tags": "mexican"}, {"title": 1}).sort({"rating_avg": -1}).limit(4)

# db.recipes.find({"likes": { $all : [1]}}, {"title": 1}).sort({"title": 1})
# db.recipes.find({"likes": { $all : [1, 35]}}, {"title": 1}).sort({"title": 1})

# db.recipes.find({"likes": { $in : [1, 35]}}, {"title": 1}).sort({"title": 1})

# db.recipes.find({"cook_time":10},{"title": 1}).explain("executionStats");

# db.recipes.getIndexes()
# db.recipes.createIndex({"cook_time": -1})

# db.recipes.dropIndex("cook_time_-1")

# db.createCollection("error_log", { capped: true, size: 10000, max: 10000 })