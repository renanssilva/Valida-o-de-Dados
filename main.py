from datetime import datetime, timedelta
from datasBr import DatasBr

# datetime.datetime -: Retorna horas exatas que estamos compilando nosso código
# datetime.timedelta

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
