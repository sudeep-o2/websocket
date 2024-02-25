import asyncio
import websockets

async def handle_websocket(websocket, _):
    while True:
        try:
            # This is a placeholder. Replace it with the actual logic to handle MongoDB change events.
            # For simplicity, this example sends a message to the client every second.
            message = "Hello from the server!"
            await websocket.send(message)
            await asyncio.sleep(1)
        except websockets.exceptions.ConnectionClosed:
            break

start_server = websockets.serve(handle_websocket, "localhost", 8000)
#print(start_server)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
