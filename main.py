from fastapi import FastAPI
import uvicorn
from ping3 import ping as ping3_ping

app = FastAPI()

def main():
    uvicorn.run("main:app", reload=True, port=13371)

@app.get("/")
async def root():
    return { "response": "Welcome to szewczukoAPI. Github: https://github.com/szewczuko/api"}

@app.get("/ping")
async def ping(ip):
    response = ping3_ping(ip)   
    if response is not None:
        return { "response": f"Ping {ip} udany! Czas odpowiedzi: {response} ms"}
    else:
        return { "response": "Ping nieudany."}
    


if __name__ == "__main__":
    main()