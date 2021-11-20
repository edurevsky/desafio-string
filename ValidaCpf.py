import re
from validate_docbr import CPF


class CPFInvalido(Exception):
    pass


class VerificaCPF(object):
    
    def __init__(self, url: str):
        self.url = url
        self.validar()


    def validar(self):
        url = self.url.strip()
        igual = url.find("=")
        cpf = url[igual + 1:]

        padrao = re.compile("[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}")
        vePadrao = padrao.match(cpf)

        if not vePadrao:
            print("Não foi encontrado um padrão tipo CPF.")
        else:
            print(f"O padrão CPF encontrado no link foi: {cpf}.")

            validacao = CPF()

            if validacao.validate(cpf):
                print("O CPF é real.\n")
            else:
                print("CPF não é real.")
                raise CPFInvalido('CPF é inválido.')
