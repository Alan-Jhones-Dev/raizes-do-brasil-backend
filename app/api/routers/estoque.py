from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.dataBase.db import get_db
from app.api.schemas import CriarEstoqueSchema
from app.api.dependencias import autorizacao_acesso
from app.infrastructure.dataBase.models import Estoque

router_estoque = APIRouter()
@router_estoque.post("/estoques", tags=["estoques"])
async def criar_estoque(dados: CriarEstoqueSchema, db: Session = Depends(get_db), usuario_logado = Depends(autorizacao_acesso(['GERENTE']))):
    novo_estoque = Estoque(
        unidade_id = dados.unidade_id,
        produto_id = dados.produto_id,
        quantidade = dados.quantidade
    )
    db.add(novo_estoque)
    db.commit()
    db.refresh(novo_estoque)
    return {
        'id': novo_estoque.id,
        'unidade_id': novo_estoque.unidade_id,
        'produto_id': novo_estoque.produto_id,
        'quantidade': novo_estoque.quantidade
    }