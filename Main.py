from ValidaCpf import *

if __name__ == "__main__":

    while True:
        print("* Verificador de CPF's a partir de URL's *")
        cpf = input("Insira a URL: ")
        try:
            VerificaCPF(cpf)

        except CPFInvalido as e:
            print(e)
