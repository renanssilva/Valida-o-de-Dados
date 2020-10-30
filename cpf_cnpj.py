from validate_docbr import CPF, CNPJ


class Documeto:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta !!!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido !!")

    def __str__(self):
        return self.formata_cpf()

    def valida(self, documento):
        validador = CPF().validate(documento)
        return validador

    def formata_cpf(self):
        mascara = CPF().mask(self.cpf)
        return mascara


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido !!")

    def __str__(self):
        return self.formata_cnpj()

    def valida(self, documento):
        validador = CNPJ().validate(documento)
        return validador

    def formata_cnpj(self):
        mascara = CNPJ().mask(self.cnpj)
        return mascara
