import requests
from acesso_cep import BuscaEnderco

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r)
# print(r.text)

cep = '08572350'

objeto_cep = BuscaEnderco(cep)
bairro, cidade, estado = objeto_cep.acessa_via_cep()
print(bairro, cidade, estado)