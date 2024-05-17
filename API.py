from fastapi import FastAPI, Query, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy.exc import IntegrityError

app = FastAPI()

# Simulando um banco de dados de atletas
atletas_db = []

# Modelo de dados para os atletas
class Atleta(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str
    categoria: str

# Endpoint para criar um novo atleta
@app.post("/atletas/")
def criar_atleta(atleta: Atleta):
    try:
        # Verificar se o atleta já está cadastrado pelo CPF
        for at in atletas_db:
            if at.cpf == atleta.cpf:
                raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o CPF: {atleta.cpf}")
        # Se não houver nenhum atleta com o mesmo CPF, adicioná-lo ao banco de dados
        atletas_db.append(atleta)
        return {"message": "Atleta cadastrado com sucesso!"}
    except IntegrityError as e:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o CPF: {atleta.cpf}")

# Endpoint para obter todos os atletas com paginação
@app.get("/atletas/", response_model=Page[Atleta])
def obter_todos_os_atletas(limit: int = Query(default=10, le=100), offset: int = Query(default=0, ge=0)):
    return paginate(atletas_db, limit=limit, offset=offset)

# Endpoint para pesquisar atletas por nome e/ou CPF
@app.get("/atletas/pesquisar/")
def pesquisar_atletas(nome: str = None, cpf: str = None):
    resultados = []
    for atleta in atletas_db:
        if (nome is None or atleta.nome == nome) and (cpf is None or atleta.cpf == cpf):
            resultados.append(atleta)
    return {"atletas": resultados}
