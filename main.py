from fastapi import FastAPI
from database import MongoDB
import controller
from fastapi import HTTPException, status
from typing import List
from models import User

app = FastAPI()

@app.post("/user", status_code=status.HTTP_201_CREATED)
async def insert_user(user: User):
    try:
        # Lógica para insertar el usuario y obtener el ID
        user = controller.InsertUser(user)
        return " User created " # Devolver el ID del usuario
    except Exception as e:
        # Si ocurre un error, lanzar una excepción HTTP con código de estado 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

from fastapi import HTTPException, status

@app.get("/user/{username}", response_model=User)
async def get_user(username: str):
    try:
        user = controller.GetUserByUsername(username)
        if user:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/users", response_model=List[User])
async def get_users():
    try:
        users = controller.GetUsers()
        if users:
            return users
        else:
            return "no users in database"
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
