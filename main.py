from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return { "response": "Welcome to szewczukoAPI. Github: https://github.com/szewczuko/api"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=13371)