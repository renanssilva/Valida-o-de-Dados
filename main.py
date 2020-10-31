from datetime import datetime, timedelta
from datasBr import DatasBr

hoje = DatasBr()
amanha = datetime.today() + timedelta(days=30)

print(hoje.tempo_cadastro())

print(amanha)

print(hoje)