import re
from validate_docbr import CPF


class NotFoundError(Exception):
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
            raise NotFoundError("Não foi padrão tipo CPF.")
        print(f"O padrão CPF encontrado no link foi: {cpf}")

        try:
            validacao = CPF()
            if validacao.validate(cpf):
                print("O CPF é real.\n")
            else:
                print("O CPF é falso.\n")
            
        except:
            pass


