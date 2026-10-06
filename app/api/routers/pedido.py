from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas import CriarPedidoSchema
from sqlalchemy.orm import Session
from app.api.dependencias import autorizacao_acesso, autenticar_acesso
from app.infrastructure.dataBase.db import get_db
from app.infrastructure.dataBase.models import Estoque
from app.infrastructure.dataBase.models import Pedido
from app.infrastructure.dataBase.models import StatusPedido
from app.infrastructure.dataBase.models import Produto_Unidade
from app.infrastructure.dataBase.models import ItemPedido
from datetime import datetime


router_pedido = APIRouter()

@router_pedido.post("/pedido", tags=["pedido"])
async def criar_novo_pedido(dados: CriarPedidoSchema, db: Session = Depends(get_db), usuario_logado = Depends(autorizacao_acesso(["ATENDENTE","CLIENTE"]))):
    for item in dados.lista_itens:
        estoque_item = db.query(Estoque).filter(Estoque.produto_id == item.produto_id, Estoque.unidade_id == dados.unidade_id).first()
        if not estoque_item or item.quantidade > estoque_item.quantidade:
            raise HTTPException(status_code=409, detail='Estoque insuficiente')

    # LAÇO PARA CALCULAR O VALOR TOTAL DO PEDIDO
    valor_total_pedido = 0
    for item in dados.lista_itens:
        preco_produto = db.query(Produto_Unidade).filter(Produto_Unidade.produto_id == item.produto_id, Produto_Unidade.unidade_id == dados.unidade_id).first()
        valor_total_pedido += (preco_produto.preco * item.quantidade)

    # INSTANCIANDO UM NOVO PEDIDO E ADICIONANDO NO BANCO
    novo_pedido = Pedido(
        canal=dados.canal,
        unidade_id=dados.unidade_id,
        status=StatusPedido.PAGAMENTO_PENDENTE,
        data = datetime.now(),
        usuario_id = usuario_logado['id'],
        valor_total = valor_total_pedido)
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    for informacao_item in dados.lista_itens:
        preco_por_item = db.query(Produto_Unidade).filter(Produto_Unidade.produto_id == informacao_item.produto_id, Produto_Unidade.unidade_id == dados.unidade_id).first()
        novo_item = ItemPedido(
            pedido_id = novo_pedido.id ,
            produto_id = informacao_item.produto_id,
            preco_unitario = preco_por_item.preco,
            quantidade = informacao_item.quantidade,
        )
        db.add(novo_item)
    db.commit()
    return {
        'nome': usuario_logado['nome'],
        'data': novo_pedido.data,
        'unidade': novo_pedido.unidade_id,
        'valor_total': novo_pedido.valor_total,
        'status_pedido': novo_pedido.status
    }


