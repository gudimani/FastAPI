from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role
from uuid import uuid4, UUID

app = FastAPI()


db: List[User] = [
    User(id=UUID("9189ef88-a9e2-4578-adf8-5c5c9b7d1770"), first_name="Pavitra", 
         last_name="G",
         gender=Gender.female,
         roles = [Role.student]),
    User(id=uuid4(), first_name="Alex", 
         last_name="B",
         gender=Gender.male,
         roles = [Role.admin, Role.user])

]

@app.get("/")
async def root():
    return {"Hello":"World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} does not exist"
    )