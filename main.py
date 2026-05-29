import asyncio
import websockets
from pylsl import StreamInlet, resolve_streams
import json

async def stream_to_websocket(websocket):
    streams = resolve_streams()
    eeg_stream = None

    for s in streams:
        if s.type() == "EEG":
            eeg_stream = s
            break

    if eeg_stream is None:
        await websocket.send(json.dumps({"error": "No EEG stream found"}))
        return

    inlet = StreamInlet(eeg_stream)

    while True:
        sample, timestamp = inlet.pull_sample()
        await websocket.send(json.dumps(sample))

async def main():
    async with websockets.serve(stream_to_websocket, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
