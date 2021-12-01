from pydantic import BaseModel


class BaseProdutoModel(BaseModel):
    id_produto: int
    produto_nome: str
    sku: str
    descricao: str

class AlterarProdutoModel(BaseModel):
    sku: str
    

class BaseCategoriaModel(BaseModel):
    id_categoria: int
    nome_categoria: str
    descricao: str

class AlterarCategoriaModel(BaseModel):
    nome_categoria: str
    descricao: str

class BaseFornecedorModel(BaseModel):
    id_Fornecedor: int
    nome_Fornecedor: str

class AlterarFornecedorModel(BaseModel):
    nome_Fornecedor: str


class BaseCompradorModel(BaseModel):
    id_Comprador: int
    nome_Comprador: str

class AlterarCompradorModel(BaseModel):
    nome_Comprador: str
