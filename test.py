from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://sudeep:Qwerty1234%40@cluster0.moe1iis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
        print(e)

db = client.test
collection = db.lol

# Set up a change stream
change_stream = collection.watch()  

# Watch for changes
for change in change_stream:
    print(change)
