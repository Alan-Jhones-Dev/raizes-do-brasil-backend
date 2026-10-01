from passlib.context import CryptContext

config_criptografia = CryptContext(schemes=['bcrypt'])

def gerar_hash(senha: str):
    return config_criptografia.hash(senha)

def verificar_senha(senha_usuario: str, senha_hash: str):
    return config_criptografia.verify(senha_usuario, senha_hash)