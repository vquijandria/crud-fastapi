from fastapi import FastAPI
from router.router import user

#App is an instance of FastAPI
app = FastAPI()



app.include_router(user)