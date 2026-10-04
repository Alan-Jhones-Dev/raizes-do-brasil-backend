from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    senha: str

class CadastrarUsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str