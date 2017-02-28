import pymongo
import datatime
import pprint
from pymongo import MongoClient

## Make a connection with mongo client
client = MongoClient()

# Getting a database
db = client.test_database

# Getting a collection
collection = db.test_collection

## Create a document
post = {"user": "Dingchao","text": "My first bud request!","tags": ["fdw"], \
		 "date": datetime.datetime.utcnow()}

# Insert a document
posts = db.posts
post_id = posts.inert_one(post).inserted_id
post_id

#After inserting the first document, the posts collection has actually 
#been created on the server. We can verify this by listing all of the 
#collections in our database:
db.collection_names(include_system_collections=False)

###Retrieve document
pprint.pprint(posts.find_one())

#Query specific post:
pprint.pprint(posts.find_one({"user": "Dingchao"}))

# Query by ObjectID
pprint.pprint(posts.find_one({"_id": post_id}))


### Bulk Inserts
new_posts = [{"user": "Dingchao","text": "My first bud request!","tags": ["fdw"], \
			"date": datetime.datetime.utcnow()}, \
			{"user": "Dingchao","text": "My first bud request!","tags": ["fdw"], \
			"date": datetime.datetime.utcnow()}]

result = posts.insert_many(new_posts)
result.inserted_ids