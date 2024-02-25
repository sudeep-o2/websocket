import asyncio
import websockets
from pymongo import MongoClient
from pymongo.server_api import ServerApi

async def handle_websocket(websocket, client, _):
    db = client.test
    collection = db.lol

    print('adwef')

    try:
        # Set up MongoDB Change Stream
        pipeline = [{"$match": {"operationType": {"$in": ["insert", "update", "replace", "delete"]}}}]
        change_stream = collection.watch(pipeline)

        print('ythg')

        async for change in change_stream:
            # Handle the change event (replace this with your custom logic)
            operation_type = change['operationType']

            if operation_type == 'insert':
                # Handle insert operation
                inserted_document = change['fullDocument']
                print(f"Document inserted: {inserted_document}")

            elif operation_type == 'update':
                # Handle update operation
                updated_document = change['fullDocument']
                print(f"Document updated: {updated_document}")

            elif operation_type == 'delete':
                # Handle delete operation
                deleted_document_id = change['documentKey']['_id']
                print(f"Document deleted with ID: {deleted_document_id}")

            else:
                # Handle other operations
                print(f"Unsupported operation type: {operation_type}")

            # Forward the data to the WebSocket clients
            await websocket.send(str(change))

    finally:
        print("Client disconnected")

if __name__ == "__main__":
    uri = "mongodb+srv://sudeep:Qwerty1234%40@cluster0.moe1iis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    start_server = websockets.serve(lambda ws, path: handle_websocket(ws, client, path), "localhost", 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
