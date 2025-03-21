from fastapi import FastAPI, HTTPException, Depends, Security
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import User, Base
from database import SessionLocal, engine
import jwt
import datetime
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

# Load environment variables
dotenv_path = "/app/.env"
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecretkey")

app = FastAPI()

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to verify JWT token
def verify_token(token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# JWT Token Generation Function
def create_token(username: str):
    payload = {"sub": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Pydantic Models for Input Validation
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# User Registration
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

# User Login
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    found_user = db.query(User).filter(User.username == user.username).first()
    if not found_user or found_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.username)
    return {"access_token": token}

# Protected Route
@app.get("/protected-route")
def protected_route(user: dict = Depends(verify_token)):
    return {"message": f"Access granted for {user['sub']}"}
