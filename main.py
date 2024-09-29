from fastapi import FastAPI, Depends, HTTPException
from oauth import get_current_user, create_access_token
from schemas import User

users_db = {
    "user1": User(username="user1", password="password1"),
    "user2": User(username="user2", password="password2"),
}

app = FastAPI()
@app.post("/token")
async def login_for_access_token(form_data: User):
    try:
        user = users_db.get(form_data.username)

        if user is None or user.password != form_data.password:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        access_token = create_access_token(data={"sub": {"user" :user.username}})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        print(123)

@app.get("/protected")
async def protected_route(username: str = Depends(get_current_user)):
    return {"message": f"Hello, {username}! This is a protected resource."}