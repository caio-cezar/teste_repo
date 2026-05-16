import os
import random
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(DATABASE_URL)

cur = conn.cursor()

# Gera CPF aleatório com 11 dígitos
cpf = ''.join(random.choices('0123456789', k=11))

cur.execute(
    """
    INSERT INTO public.clientes (cpf, nome, pais)
    VALUES (%s, %s, %s)
    """,
    (cpf, "Caio Pedro", "Portugal")
)

conn.commit()

print(f"Cliente inserido com CPF: {cpf}")

cur.close()
conn.close()
