import asyncio
import json
import websockets
from pymongo import MongoClient 

async def handle_websocket(websocket, _):
    print('5')
    while True:
        print('6')
        message = await websocket.recv()
        print('message',message)
        await websocket.send(message)

async def handle_change_stream(cursor):
    for change in cursor:
        print(change)
        await websocket.send(json.dumps(change))

async def main():
    client = MongoClient("mongodb+srv://sudeep:Qwerty1234%40@cluster0.moe1iis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client.test
    collection = db.lol
    print('1')
    cursor = collection.watch()
    print('2')

    async with websockets.serve(handle_websocket, "localhost", 8765):
        print('3')
        asyncio.create_task(handle_change_stream(cursor))
        print('4')
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
