import os
import pandas as pd
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(DATABASE_URL)

# Faz o SELECT da tabela
query = """
SELECT *
FROM public.clientes
"""

# Carrega os dados em um DataFrame
df = pd.read_sql(query, conn)

# Gera o CSV
df.to_csv("clientes.csv", index=False)

print("CSV gerado com sucesso")

conn.close()
