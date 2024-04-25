import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Welcome to the network"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=5000)


