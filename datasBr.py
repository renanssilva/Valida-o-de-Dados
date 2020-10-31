from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes = self.momento_cadastro.month - 1
        return meses_do_ano[mes]

    def dia_semana(self):
        dias_da_semana = [
            "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"
        ]
        dia = self.momento_cadastro.weekday()
        return dias_da_semana[dia]

    # Mascara
    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=30) - self.momento_cadastro
        return tempo_cadastro