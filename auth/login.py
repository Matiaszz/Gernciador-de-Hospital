def teste(nome, email, senha):
    if nome and email and senha:

        print(f'{nome} | {email} | {senha}')
        return True
    return False


def teste_login(email, senha):
    if email and senha:
        print(f'{email} | {senha}')
        return True
    return False
