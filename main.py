from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class App(BaseModel):
    id: str
    appdata: str | None = None
    name: str | None = None
    description: str | None = None


@app.get("/")
def get_root():
    return {"greeting": "Hello world!"}
    # return {"Hello world!"}


@app.get("/apps")
def get_app_list():
    # TODO: Return App
    return [
        {
            "app_id": "test",
            "name": "Name",
            "description": "Lorem ipsum dolor sit amet",
        },
        {
            "app_id": "test 2",
            "name": "Name",
            "description": "Lorem ipsum dolor sit amet",
        },
    ]


@app.get("/apps/{app_id}")
def get_app(app_id: str):
    # TODO: Return App
    return {
        "app_id": app_id,
        "name": "Name",
        "description": "Lorem ipsum dolor sit amet",
    }


# add information for commit (name, email address)
@app.put("/apps/{app_id}")
def put_app(app_id: str, app: App):
    return app
