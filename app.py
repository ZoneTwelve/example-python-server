from fastapi import FastAPI, Request
from datetime import datetime
import uvicorn

app = FastAPI()
start_time = datetime.now()

@app.get("/health")
async def health():
    uptime = datetime.now() - start_time
    return {"status": "ok", "uptime": str(uptime)}

@app.get("/hello")
async def hello(username: str):
    return {"message": f"Hello {username}"}

@app.get("/ping")
async def ping():
    return {"response": "pong"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
