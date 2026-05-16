import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(DATABASE_URL)

cur = conn.cursor()

cur.execute(
    """
    INSERT INTO public.clientes (cpf, nome, pais)
    VALUES (%s, %s, %s)
    """,
    ("12312312332", "Caio Pedro", "Portugal")
)

conn.commit()

print("Cliente inserido")

cur.close()
conn.close()
