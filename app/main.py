from fastapi import FastAPI
from app.api.routers.auth import router_auth
from app.api.routers.usuarios import router_usuario

system = FastAPI()
system.include_router(router_auth)
system.include_router(router_usuario)

