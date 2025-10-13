# gerar_novo_hash.py
import bcrypt

# A senha que queremos usar
password = b"P10$2025grupo6"

# Gerando o hash no seu computador
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("--- NOVO HASH GERADO ---")
print("Copie a linha abaixo e cole no seu arquivo secrets.toml:")
print(hashed.decode())
print("--------------------------")