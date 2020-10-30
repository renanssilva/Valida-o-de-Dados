from cpf_cnpj import Documeto
from validate_docbr import CNPJ
renan_cpf = "40860090809"
ex_cnpj = "35379838000112"

doc_cpf_1 = Documeto.cria_documento(renan_cpf)
doc_cnpj_1 = Documeto.cria_documento(ex_cnpj)

print(doc_cnpj_1)
print(doc_cpf_1)
