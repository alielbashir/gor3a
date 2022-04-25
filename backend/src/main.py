from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.core import generate_pairs


app = FastAPI()


# A list of giftswaps from different users with int id as key
DB: dict[int, dict[str, str]] = {}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/giftswap", status_code=201)
async def create_giftswap(people: list[str]):
    """
    Takes a list of participants' names
    adds users to the giftswap
    returns giftswap ID
    """
    # generate a unique id for the gift swap
    id = len(DB)
    # generate a dict of pairs for the gift swap
    pairs = generate_pairs(people)
    # add the gift swap to the database
    DB[id] = pairs
    return {"id": id}


@app.get("/giftswap/{id}/{gifter}", status_code=200)
async def get_giftswap(id: int, gifter: str):
    """
    Takes a giftswap ID and a gifter's name
    returns the receiver's name,
    or 404 if the gift swap doesn't exist

    can only be accessed once
    """
    # get the gift swap from the database
    try:    
        if (receiver := DB[id][gifter]) is None:
            raise HTTPException(
                status_code=403, detail="This gifter has already viewed their receiver"
            )
        DB[id][gifter] = None
    except KeyError:
        raise HTTPException(status_code=404, detail="GiftSwap not found")

    # return the receiver's name
    return {"receiver": receiver}
