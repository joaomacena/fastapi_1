from typing import List
from fastapi import status,APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
import schemas

loja = APIRouter()

mercado_produtos = []
mercado_Categorias = []
mercado_Fornecedores = []
mercado_Compradores = []


def remover_da_lista(Variavel_deletar,lista):
    resultado = list(filter(lambda a: a[1].Variavel_deletar == Variavel_deletar, enumerate(lista)))
    print(resultado)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{Variavel_deletar} nao foi encontrado em {lista.__class__.__name__}')

    i, _ = resultado[0]
    del lista[i]



@loja.post(
    '/mercado',
    tags=["Produto"],
    response_model=schemas.BaseProdutoModel, 
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo produto"
    )
def adicionar_produto(produto:schemas.BaseProdutoModel):
    mercado_produtos.append(produto)
    return produto


@loja.get(
    '/mercado',
    tags=["Produto"],
    response_model=List[schemas.BaseProdutoModel],
    status_code=status.HTTP_200_OK
    )
def lista_produtos():
    return mercado_produtos


@loja.delete(
    '/mercado/{sku}',
    tags=["Produto"],
    status_code=status.HTTP_204_NO_CONTENT
    )
def remover_produto(sku: str):
    return remover_da_lista(sku,mercado_produtos)


@loja.put(
    '/mercado/{sku}',
    tags=["Produto"]
    )
def alterar_produto(sku: str, produto: schemas.AlterarProdutoModel):
    resultado = list(filter(lambda a: a.sku == sku, mercado_produtos))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Produto com o sku: {sku} nao foi encontrado')
    produto_encontrado = resultado[0]
    produto_encontrado.id_produto = produto.id_produto
    produto_encontrado.produto_nome = produto.produto_nome
    produto_encontrado.sku = produto.sku
    produto_encontrado.descricao = produto.descricao

    return produto_encontrado


@loja.patch(
    '/mercado/alterar-sku/{sku}',
    tags=["Produto"]
    )
def alterar_cpf_produto(sku: str, sku_novo: str = Body(...)):
    resultado = list(filter(lambda a: a.sku == sku, mercado_produtos))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Produto com o sku: {sku} nao foi encontrado')

    produto_encontrado = resultado[0]
    produto_encontrado.sku = sku_novo

    return produto_encontrado


@loja.post(
    '/categoria',
    tags=["Categoria"],
    response_model=schemas.BaseCategoriaModel,
    status_code=status.HTTP_201_CREATED,
    summary="Criar uma nova categoria"
    )
def adicionar_categoria(categoria:schemas.BaseCategoriaModel):
    mercado_Categorias.append(categoria)
    return categoria


@loja.get(
    '/categoria',
    tags=["Categoria"],
    response_model=List[schemas.BaseCategoriaModel],
    status_code=status.HTTP_200_OK,
    )
def lista_categorias():
    return mercado_Categorias


@loja.delete(
    '/categoria/{id_categoria}',
    tags=["Categoria"], 
    status_code=status.HTTP_204_NO_CONTENT
    )
def remover_categoria(id_categoria: int):
    return remover_da_lista(id_categoria,mercado_Categorias)


@loja.put(
    '/categoria/{id_categoria}',
    tags=["Categoria"]
    )
def alterar_categoria(id_categoria: int, categoria: schemas.AlterarCategoriaModel):
    resultado = list(filter(lambda a: a.id_categoria == id_categoria, mercado_Categorias))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'A categoria com o id : {id_categoria} nao foi encontrado')

    categoria_encontrado = resultado[0]
    categoria_encontrado.produto_nome = categoria.nome_categoria
    categoria_encontrado.descricao = categoria.descricao

    return categoria_encontrado


@loja.patch(
    '/categoria/categoria-id_categoria/{id_categoria}',
    tags=["Categoria"]
    )
def alterar_id_fornecedor(id_categoria: int, id_novo: str = Body(...)):
    resultado = list(filter(lambda a: a.id_categoria == id_categoria, mercado_Categorias))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'A categoria com o id : {id_categoria} nao foi encontrado')

    categoria_encontrado = resultado[0]
    categoria_encontrado.id_categoria = id_novo

    return categoria_encontrado


@loja.post(
    '/fornecedor',
    tags=["Fornecedor"],
    response_model=schemas.BaseFornecedorModel, 
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo fornecedor" 
    )
def adicionar_fornecedor(fornecedor:schemas.BaseFornecedorModel):
    mercado_Fornecedores.append(fornecedor)
    return fornecedor


@loja.get(
    '/fornecedor',
    tags=["Fornecedor"],
    response_model=list[schemas.BaseFornecedorModel], 
    status_code=status.HTTP_200_OK,
    )
def lista_fornecedor():
    return mercado_Fornecedores


@loja.delete(
    '/fornecedor/{id_Fornecedor}',
    tags=["Fornecedor"],
    status_code=status.HTTP_204_NO_CONTENT
    )
def remover_fornecedor(id_Fornecedor: int):
    return remover_da_lista(id_Fornecedor,mercado_Fornecedores)


@loja.put(
    '/fornecedor/{id_Fornecedor}',
    tags=["Fornecedor"]
    )
def alterar_fornecedor(id_Fornecedor: int, fornecedor: schemas.AlterarFornecedorModel):
    resultado = list(filter(lambda a: a.id_Fornecedor == id_Fornecedor, mercado_Fornecedores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'A fornecedor com o id : {id_Fornecedor} nao foi encontrado')

    fornecedor_encontrado = resultado[0]
    fornecedor_encontrado.nome_Fornecedor = fornecedor.nome_Fornecedor

    return fornecedor_encontrado


@loja.patch(
    '/fornecedor/categoria-id_categoria/{id_categoria}',
    tags=["Fornecedor"]
    )
def alterar_id_fornecedor(id_categoria: int, id_novo: str = Body(...)):
    resultado = list(filter(lambda a: a.id_categoria == id_categoria, mercado_Categorias))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Produto com o sku: {id_categoria} nao foi encontrado')

    categoria_encontrado = resultado[0]
    categoria_encontrado.id_categoria = id_novo

    return categoria_encontrado


@loja.post(
    '/comprador',
    tags=["Comprador"],
    response_model=schemas.BaseCompradorModel, 
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo comprador" 
    )
def adicionar_comprador(comprador:schemas.BaseCompradorModel):
    mercado_Compradores.append(comprador)
    return comprador


@loja.get(
    '/comprador',
    tags=["Comprador"],
    response_model=list[schemas.BaseFornecedorModel], 
    status_code=status.HTTP_200_OK,
    )
def lista_comprador():
    return mercado_Compradores


@loja.delete(
    '/comprador/{id_Comprador}',
    tags=["Comprador"],
    status_code=status.HTTP_204_NO_CONTENT
    )
def remover_comprador(id_Comprador: int):
    return remover_da_lista(id_Comprador,mercado_Compradores)


@loja.put(
    '/comprador/{id_Comprador}',
    tags=["Comprador"]
    )
def alterar_fornecedor(id_Comprador: int, comprador: schemas.AlterarCompradorModel):
    resultado = list(filter(lambda a: a.id_Comprador == id_Comprador, mercado_Compradores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'A comprador com o id : {id_Comprador} nao foi encontrado')

    comprador_encontrado = resultado[0]
    comprador_encontrado.nome_Comprador = comprador.nome_Comprador

    return comprador_encontrado


@loja.patch(
    '/fornecedor/categoria-id_categoria/{id_Comprador}',
    tags=["Comprador"]
    )
def alterar_id_fornecedor(id_Comprador: int, id_comprador: str = Body(...)):
    resultado = list(filter(lambda a: a.id_Comprador == id_Comprador, mercado_Compradores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'A comprador com o id : {id_Comprador} nao foi encontrado')

    comprador_encontrado = resultado[0]
    comprador_encontrado.id_comprador = id_comprador

    return comprador_encontrado