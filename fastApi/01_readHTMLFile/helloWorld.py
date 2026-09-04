from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Show hello world
# @app.get("/")
# async def root():
#   return {"message": "Hello World"}

# 1. Чтения html файла по гет запросу
@app.get("/")
def root():
  return FileResponse("./index.html")

# 2. Альтернатива - чтения html файла по гет запросу
@app.get("/file", response_class = FileResponse)
def root_html():
    return "public/index.html"