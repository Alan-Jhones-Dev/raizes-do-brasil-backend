from fastapi import FastAPI
from app.api.routers.auth import router_auth
from app.api.routers.usuarios import router_usuario
from app.api.routers.produto import router_produto
from app.api.routers.produto_unidade import router_produto_unidade
from app.api.routers.unidade import router_unidade
from app.api.routers.estoque import router_estoque
from app.api.routers.pedido import router_pedido

system = FastAPI()
system.include_router(router_auth)
system.include_router(router_usuario)
system.include_router(router_produto)
system.include_router(router_produto_unidade)
system.include_router(router_unidade)
system.include_router(router_estoque)
system.include_router(router_pedido)


