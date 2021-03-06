# import datetime module
import datetime
# import pymongo module
import pymongo
# import os for env var
import os
usr = os.environ['MONGO_DB_USER']
pwd = os.environ['MONGO_DB_PASS']
# connection string
client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@firstcluster-obuqd.mongodb.net/test?retryWrites=true&w=majority")
# test
db = client['SampleDatabase']
# define collection
collection = db['SampleCollection']
# sample data
document = {"company":"Capital One",
	"city":"McLean",
	"state":"VA",
	"country":"US"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
print(id)
