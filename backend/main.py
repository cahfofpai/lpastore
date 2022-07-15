from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"])

class App(BaseModel):
    id: str
    appdata: str | None = None
    name: str | None = None
    description: str | None = None
    mobile_compatibility: int | None = None


@app.on_event("startup")
def startup():
    # generated with `figlet -w 50 -c Welcome to LPAStore -f slant`
    print(
        """
     _       __     __                        
    | |     / /__  / /________  ____ ___  ___ 
    | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \\
    | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/
    |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/ 
                                              
                      __      
                     / /_____ 
                    / __/ __ \\
                   / /_/ /_/ /
                   \__/\____/ 
                              
      __    ____  ___   _____ __                
     / /   / __ \/   | / ___// /_____  ________ 
    / /   / /_/ / /| | \__ \/ __/ __ \/ ___/ _ \\
   / /___/ ____/ ___ |___/ / /_/ /_/ / /  /  __/
  /_____/_/   /_/  |_/____/\__/\____/_/   \___/ 
    """
    )

    # TODO: Make data dir configurable
    if not os.path.exists("../data"):
        os.makedirs("../data")
        # TODO: Unified logging
        print("Data dir created")

    if not os.path.exists("../data/apps"):
        os.makedirs("../data/apps")
        # TODO: Unified logging
        print("Dir ../data/apps created")


@app.get("/")
def get_root():
    return {"greeting": "Hello world!"}


@app.get("/apps")
def get_app_list():
    dir = "../data/apps/"
    apps: list[App] = []
    for file in os.listdir(dir):
        apps.append(App.parse_file(f"{dir}{file}"))
    return apps


@app.get("/apps/{id}")
def get_app(id: str):
    try:
        return App.parse_file(f"../data/apps/{id}.json")
    except:
        # TODO: Other status code when file can not be parsed (although this should not happen)
        raise HTTPException(404)


# TODO: Add information for commit (name, email address, message)
@app.put("/apps/{id}")
def update_app(id: str, app: App):
    with open(f"../data/apps/{id}.json", "w") as file:
        file.write(json.dumps(app.dict(), indent=4))
    # TODO: Does it make sense to return the app here?
    return app
