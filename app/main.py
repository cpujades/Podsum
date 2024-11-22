from fastapi import FastAPI

from mangum import Mangum
import uvicorn

from app.routers import transcription

app = FastAPI()
handler = Mangum(app)

app.include_router(transcription.router)


@app.get("/")
def read_root():
    return {"Status": "Hello World! Main app working fine."}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)