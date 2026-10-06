from pydantic import BaseModel, field_validator
from app.infrastructure.dataBase.models import CanalPedido
from app.infrastructure.dataBase.models import CategoriaProduto



class LoginSchema(BaseModel):
    email: str
    senha: str


class CadastrarUsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str
    @field_validator('perfil')
    @classmethod
    def aumentar_letra(cls, valor):
        return valor.upper()


class ItemPedidoSchema(BaseModel):
    quantidade: int
    produto_id: int


class CriarPedidoSchema(BaseModel):
    canal: CanalPedido
    unidade_id: int
    lista_itens: list[ItemPedidoSchema]


class CriarUnidadeSchema(BaseModel):
    nome: str
    endereco: str
    telefone: str
    regiao: str


class CriarProdutoSchema(BaseModel):
    nome:str
    descricao:str
    categoria: CategoriaProduto


class CriarProdutoUnidadeSchema(BaseModel):
    preco: float
    unidade_id: int
    produto_id: int


class CriarEstoqueSchema(BaseModel):
    unidade_id: int
    produto_id: int
    quantidade: int
