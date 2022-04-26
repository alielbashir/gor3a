from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.core import generate_pairs

URL = "http://localhost:8000"

app = FastAPI()


# A list of gor3as from different users with int id as key
DB: dict[int, dict[str, str]] = {}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/gor3a", status_code=201)
async def create_gor3a(people: list[str]):
    """
    Takes a list of participants' names
    adds users to the gor3a
    returns gor3a ID
    """
    # generate a unique id for the gift swap
    id = len(DB)
    # generate a dict of pairs for the gift swap
    pairs = generate_pairs(people)
    # add the gift swap to the database
    DB[id] = pairs
    return {"id": id}


@app.get("/gor3a/{id}/{gifter}", status_code=200)
async def get_gor3a_receiver(id: int, gifter: str):
    """
    Takes a gor3a ID and a gifter's name
    returns the receiver's name,
    or 404 if the gift swap doesn't exist

    can only be accessed once
    """
    # get the gift swap from the database
    try:
        receiver = DB[id][gifter]
        receiver_name = receiver.name
        if receiver.viewed:
            raise HTTPException(
                status_code=403, detail="This gifter has already viewed their receiver"
            )
        DB[id][gifter].viewed = True
        DB[id][gifter].name = None
    except KeyError:
        raise HTTPException(status_code=404, detail="gor3a not found")

    # return the receiver's name
    return {"receiver": receiver_name}


@app.get("/gor3a/{id}", status_code=200)
async def get_gor3a(id: int):
    """
    Takes a gor3a ID
    returns the receiver's URLS,
    or 404 if the gift swap doesn't exist
    can only be accessed once
    """

    urls = []

    try:
        if (gor3a := DB[id]) is None:
            raise HTTPException(status_code=403, detail="This gor3a doesn't exist")
        urls = [
            {"name": gifter, "url": f"{URL}/gor3a/{id}/{gifter}", "viewed": DB[id][gifter].viewed}
            for gifter in gor3a
        ]
    except KeyError:
        raise HTTPException(status_code=404, detail="gor3a not found")

    # return the receiver's name
    return {"urls": urls}
