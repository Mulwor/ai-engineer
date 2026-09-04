from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

# add new marhrute
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}
