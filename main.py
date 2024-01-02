from fastapi import FastAPI
import uvicorn
from ping3 import ping as ping3_ping
import random
import requests
import yaml
from fastapi.responses import RedirectResponse
import starlette.status as status
app = FastAPI()

def main():
    uvicorn.run("main:app", reload=True, port=13371, host="0.0.0.0")

@app.get("/")
async def root():
    return { "response": "Welcome to szewczukoAPI. Github: https://github.com/szewczuko/api"}

@app.get("/security")
async def security():
    return RedirectResponse(
        url="https://github.com/szewczuko/api/blob/main/SECURITY.md", status_code=status.HTTP_302_FOUND
    )

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
async def randomizer(url):
    rp = requests.get(url)
    content = rp.text
    lines = content.splitlines()
    random_text = random.choice(lines)
    return { "response": random_text}
    
@app.get("/8ball")
async def eight_ball():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
        responses = config["8ball_responses"]
        random_response = random.choice(responses)
        return { "response": random_response}

if __name__ == "__main__":
    main()