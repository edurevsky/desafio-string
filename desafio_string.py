import re

class NotFoundError(Exception):
    pass


class BuscaCpf(object):
    def __init__(self, url: str):
        self.url = url


    def verificar(self):
        url = self.url
        igual = url.find("=")
        base = url[0:igual]
        cpf = url[igual + 1:]

        padrao = re.compile("[0-9]{3}(.)?[0-9]{3}(.)?[0-9]{3}(-)?[0-9]{2}")
        vePadrao = padrao.match(cpf)

        if not vePadrao:
            raise NotFoundError("Não foi achado um CPF.")
        print(f"O CPF encontrado no link foi: {cpf}")


BuscaCpf("https://www.bytebank.com.br/valida?cpf=12345678910").verificar()
BuscaCpf("https://www.bytebank.com.br/valida?cpf=123.456.789-10").verificar()
