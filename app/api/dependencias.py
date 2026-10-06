from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from app.infrastructure.security.jwt import validar_token
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def autenticar_acesso(token: str = Depends(oauth2_scheme)):
    try:
        token_autenticado = validar_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Autenticação invalida")
    return token_autenticado

def autorizacao_acesso(perfil_autorizado: list):
    def fabrica_permissao(usuario: dict = Depends(autenticar_acesso)):
        if usuario["perfil"] in perfil_autorizado:
            return usuario
        else:
            raise HTTPException(status_code=403, detail='Usuario nao autorizado')
    return fabrica_permissao
