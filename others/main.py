from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from cubox_sync import sync_job

app = FastAPI()


# Request model
class SyncRequest(BaseModel):
    refresh_token: str
    cubox_api_key: str


@app.post("/start")
async def start_sync(sync_request: SyncRequest):
    # Call the function to start the sync job
    sync_job(sync_request.refresh_token, sync_request.cubox_api_key)

    return {"detail": "Sync job started"}


uvicorn.run("main:app")  # Assuming the file is main.py
