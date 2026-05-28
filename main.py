import asyncio
import websockets
from pylsl import StreamInlet, resolve_streams
import json

async def stream_to_websocket(websocket):
    # EEG ストリームを探す
    streams = resolve_streams(prop='type', value='EEG')
    inlet = StreamInlet(streams[0])

    while True:
        sample, timestamp = inlet.pull_sample()
        await websocket.send(json.dumps(sample))

async def main():
    async with websockets.serve(stream_to_websocket, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
