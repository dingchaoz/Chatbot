import pymongo
import datetime
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
new_posts = [{"user": "Ryan","text": "My first bud request!","tags": ["fdw"], \
			"date": datetime.datetime.utcnow()}, \
			{"user": "Mike","text": "My first bud request!","tags": ["fdw"], \
			"date": datetime.datetime.utcnow()}]

result = posts.insert_many(new_posts)
result.inserted_ids

##Update query http://stackoverflow.com/questions/33189258/append-item-to-mongodb-document-array-in-pymongo-without-re-insertion
# update a field of existing post
#https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify
#https://docs.mongodb.com/v3.2/reference/method/db.collection.updateOne/

##Insert a new tag in the tags field array
posts.update_one({'user':'Dingchao'},{'$push': {'tags': 'new_tag'}})

##Insert a new field called tags2 and add the first element as new_tag2
posts.update_one({'user':'Dingchao'},{'$set': {'tags2': ['new_tag2']}})

# Update the date
posts.update_one({'user':'Dingchao'},{'$set': {'date': datetime.datetime.utcnow()}}