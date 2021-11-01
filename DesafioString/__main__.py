from __init__ import *

if __name__ == "__main__":
    rodando = True


    while rodando:
        print("* Verificador de CPF's a partir de URL's *")
        stringcpf = input("Insira a URL: ")
        try:
            VerificaCPF(stringcpf)
        except:
            pass