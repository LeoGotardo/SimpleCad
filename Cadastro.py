import os

def menu():
    ind = print(f"Oque quer fazer agora?\n1-Tentar Novamente\n2-Sair\n")
    
    if ind == "1":
        main()
    elif ind == "2":
        exit()
    else:
        print(f"Opção invalida tente novamente.")
        os.system("cls")
        menu()
        
def cad():
    os.system("cls")

    log = input(print(f"Loguin:"))
    pess = input(print(f"\nSenha:"))
    senha_v = input(print(f"\nConfirme a senha:"))

    while pess != senha_v:
        os.system("cls")

        print(f"Suas senhas não coecidem, tente novamente.")

        pess = input(print(f"Senha:"))
        senha_v = input(print("\nConfirme a senha:"))

    cred = [log,pess]
    
    add(log, pess)

    os.system("cls")
    print(f"\nSuas credenciais são:{cred}")

def log():
    os.system("cls")
    loguin = input(print(f"Loguin:"))
    pess = input(print(f"\nSenha:"))
    
    if read(loguin, pess) == True:
        print(f"Loguin concluido, bem-vindo {loguin}\n.")
    
    else:
        ind = input(print(f"Credenciais não reconhecidas\n1-Deseja tentar novamente?\n2-Ir para criação de credenciais. "))
        
        if ind == 1:
            log()
        elif ind == 2:
            cad()
        else:
            os.system("cls")
            ind = input(print(f"Credenciais não reconhecidas\n1-Deseja tentar novamente?\n2-Ir para criação de credenciais. "))

def add(log, pess):
    cred = [log, pess]
    with open("belle.txt","a+", encoding = "utf-8") as arquivo:
        arquivo.write("Loguin:{}\n".format(cred[0]))
        arquivo.write("Senha:{}\n".format(cred[1]))

def read(ind_log, ind_pess):
    with open("belle.txt", "r", encoding = "utf-8") as arquivo:
        mensagem = arquivo.readlines()

    for linha in mensagem:
        if ind_log and ind_pess in linha:
            return True
        else:
            return False    

def main():
    ind = input(print(f"Oque deseja fazer?\n1-Cadastro\n2-Loguin\n"))

    if ind == "1" or ind == "Cadastro" or ind == "cadastro":
        cad()
    elif ind == "2" or ind == "Loguin" or ind == "loguin":
        log()
    else:
        print(f"Opção invalida.")
        main()

    menu()

main() 
