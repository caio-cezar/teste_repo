import pandas as pd
import requests

x = requests.get('https://api.maisretorno.com/v3/general/quotes/ihfa:idx?adjusted=true').json()

print('Requisicao realizada com sucesso.')
print(x)