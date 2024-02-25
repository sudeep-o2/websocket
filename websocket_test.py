
import websocket

def on_message(ws, message):
    print(f"Received: {message}")

ws = websocket.WebSocketApp("ws://localhost:8765", on_message=on_message)
ws.run_forever()
