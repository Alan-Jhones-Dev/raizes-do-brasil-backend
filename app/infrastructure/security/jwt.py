import os
from dotenv import load_dotenv
from jose import jwt
load_dotenv()

secret_key = os.environ['JWT_TOKEN']
algorithm_secret =os.environ['JWT_ALGORITHM']

def criar_token(dados: dict):

    token = jwt.encode(dados, secret_key, algorithm=algorithm_secret)
    return token

def validar_token(token: str):
    return jwt.decode(token, secret_key, algorithms=[algorithm_secret])

