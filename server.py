from flask import Flask
import subprocess

app = Flask(__name__)
process = None

@app.post("/start")
def start_stream():
    global process
    if process is None:
        process = subprocess.Popen(["muselsl", "stream"])
        return "muselsl stream started"
    return "Already running"

@app.post("/stop")
def stop_stream():
    global process
    if process is not None:
        process.terminate()
        process = None
        return "muselsl stream stopped"
    return "Not running"

if __name__ == "__main__":
    app.run(port=5000)
