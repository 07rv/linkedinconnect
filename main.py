from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from oauth import get_current_user, create_access_token

import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        USERNAME = os.getenv('USER_NAME_LOGIN')
        USERPASSWORD = os.getenv('USER_PASSWORD_LOGIN')
        
        if USERNAME != form_data.username or USERPASSWORD != form_data.password:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        access_token = create_access_token(data={"sub": {"user" : USERNAME}})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        print(e)

@app.get("/protected")
async def protected_route(username: str = Depends(get_current_user)):
    return {"message": f"Hello, {username}! This is a protected resource."}