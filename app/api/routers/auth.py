from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas import LoginSchema
from sqlalchemy.orm import Session
from app.infrastructure.dataBase.db import get_db
from app.infrastructure.dataBase.models import Usuario
from app.domain.hashes import verificar_senha
from app.infrastructure.security.jwt import criar_token

router_auth = APIRouter()


@router_auth.post("/login")
async def login_usuario(dados: LoginSchema, db: Session = Depends(get_db)):
    busca_email = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if busca_email:
        dict_usuario = {
            'id': busca_email.id,
            'perfil': busca_email.perfil,
            'unidade': busca_email.unidade_id,
        }
        if verificar_senha(dados.senha, busca_email.senha_hash):
            token = criar_token(dict_usuario)
            return {'token': token}
        else:
            raise HTTPException(status_code=400, detail="Senha incorreta")

    else:
        raise HTTPException(status_code=400, detail="Email não encotrado no sistema")

