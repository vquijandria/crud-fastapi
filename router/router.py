from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.user_schema import User
from config.db import engine, SessionLocal
from model.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.params import Depends
import model
import schema.user_schema as schema



user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hello World from user router"}


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



#Create user
@user.post('/users/',response_model=schema.User)
def create_users(entrada:schema.User,db:Session=Depends(get_db)):
    usuario = model.users.User(username = entrada.username,nombre=entrada.nombre,rol=entrada.rol,estado=entrada.estado)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

