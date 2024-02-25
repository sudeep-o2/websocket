"""from pymongo import MongoClient
from bson.json_util import dumps
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import ssl

# Replace these with your MongoDB Atlas username and password
username = "sudeep"
password = "Qwerty1234@"

# Replace these with your MongoDB Atlas connection details
cluster_address = "cluster0.moe1iis.mongodb.net"
database_name = "sample_airbnb"

# Escape the username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the connection string with escaped username and password
connection_string = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_address}/{database_name}?retryWrites=true&w=majority"

# Rest of your code remains unchanged
# Connect to MongoDB Atlas
client = MongoClient(connection_string,server_api=ServerApi('1'),ssl_cert_reqs=ssl.CERT_NONE)
db = client[database_name]
collection_name = "candidate"
collection = db[collection_name]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)"""


# Insert a document into the collection
"""document_to_insert = {
  
}
result = collection.insert_one(document_to_insert)
print(f"Inserted document with ID: {result.inserted_id}")

# Define a change stream on the collection
change_stream = collection.watch(full_document='updateLookup')

# Iterate over the change stream
for change in change_stream:
    # Handle the change event (replace this with your custom logic)
    operation_type = change['operationType']

    if operation_type == 'insert':
        # Handle insert operation
        inserted_document = change['fullDocument']
        print(f"Document inserted: {dumps(inserted_document)}")

   
"""
import asyncio
import websockets
from pymongo import MongoClient
print('hi')
async def handle_websocket(websocket, path):
    print("Client connected")

    client = MongoClient("mongodb+srv://sudeep:Qwerty1234%40@cluster0.moe1iis.mongodb.net/?retryWrites=true&w=majority")
    db = client["rdt"]
    collection = db["test"]
    
    d={"name":"base"}

    try:
        async for message in websocket:
            print(f"Received message: {message}")
            # Perform MongoDB operations based on the received message
            # For example, insert the message into a collection
            result = collection.insert_one(d)
            print(f"Inserted document: {result.inserted_id}")
            # Echo the message back to the client
            await websocket.send(message)
    except Exception as e :
        print(e,'Error')
    finally:
        print("Client disconnected")
print('lol')
start_server = websockets.serve(handle_websocket, "localhost", 8000)
print('lol2')
asyncio.get_event_loop().run_until_complete(start_server)
print('lol3')
asyncio.get_event_loop().run_forever()
