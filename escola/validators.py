import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
        cpf = CPF()
        cpf_invalido = cpf.validate(numero_cpf)
        return not cpf_invalido

def nome_invalido(nome):
        return not nome.isalpha()

def celular_invalido(celular):
        #99 99999-9999
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, celular)
        return not resposta