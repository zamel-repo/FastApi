from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
async def getAllUsers():
    response = [
        {"user_id": 1, "name": "Alice"},
        {"user_id": 2, "name": "Bob"},
        {"user_id": 3, "name": "Charlie"}
    ]
    return response

@router.post(
            "/{user_name}", 
             summary= "sign up a new user",
             description="Create a new user with the given user name"
             )
async def addUser(user_name: str):
    new_user = {"user_id": 4, "name": user_name}
    return {"message": "User added successfully", "user": new_user}