from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import configparser
import os
import json

app = FastAPI()

# Load config
config = configparser.ConfigParser()
config.read("config.ini")

DATA_DIR = config["Main"]["DataDir"]

APPS_DIR = f"{DATA_DIR}/apps"

# Allow cross origin requests from frontend

origins = [
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"])

# data models

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

    # create dir structure for data if it does not exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        # TODO: Unified logging
        print("Data dir created")

    if not os.path.exists(APPS_DIR):
        os.makedirs(APPS_DIR)
        # TODO: Unified logging
        print(f"Dir {APPS_DIR} created")

# endpoints

@app.get("/")
def get_root():
    app_count = len(os.listdir(APPS_DIR))
    return {"app_count": app_count}


@app.get("/apps")
def get_app_list():
    apps: list[App] = []
    for file in os.listdir(APPS_DIR):
        apps.append(App.parse_file(f"{APPS_DIR}/{file}"))
    return apps


@app.get("/apps/{id}")
def get_app(id: str):
    try:
        return App.parse_file(f"{APPS_DIR}/{id}.json")
    except:
        # TODO: Other status code when file can not be parsed (although this should not happen)
        raise HTTPException(404)


# TODO: Add information for commit (name, email address, message)
@app.put("/apps/{id}")
def update_app(id: str, app: App):
    with open(f"{APPS_DIR}/{id}.json", "w") as file:
        file.write(json.dumps(app.dict(), indent=4))
    # TODO: Does it make sense to return the app here?
    return app
