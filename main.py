import asyncio
import websockets
from pylsl import StreamInlet, resolve_streams

async def stream_to_websocket(websocket):
    streams = resolve_streams('type', 'EEG')
    inlet = StreamInlet(streams[0])

    while True:
        sample, _ = inlet.pull_sample()
        await websocket.send(str(sample))

async def main():
    async with websockets.serve(stream_to_websocket, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
