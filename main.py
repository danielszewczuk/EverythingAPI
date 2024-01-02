from fastapi import FastAPI
import uvicorn
from ping3 import ping as ping3_ping
import random
import requests

app = FastAPI()

def main():
    uvicorn.run("main:app", reload=True, port=13371, host="0.0.0.0")

@app.get("/")
async def root():
    return { "response": "Welcome to szewczukoAPI. Github: https://github.com/szewczuko/api"}

@app.get("/ping")
async def ping(ip):
    response = ping3_ping(ip)   
    if response is not None and response is not False:
        response = response * 1000
        response = round(response, 2)
        return { "response": f"Ping {ip} udany! Czas odpowiedzi: {response} ms"}
    else:
        return { "response": "Ping nieudany."}
    
@app.get("/randomizer")
async def randomizer(link):
    txt = requests.get(link)
    fcontent = txt.text
    reply = random.choice(open(fcontent).readlines())
    return { "response": reply}
if __name__ == "__main__":
    main()