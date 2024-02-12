import random
import string

def gerar_chave_secreta(comprimento=16, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=False):
    """
    Gera uma chave secreta/senha com base nos parâmetros fornecidos.

    Parâmetros:
        comprimento (int): Comprimento da chave/senha (padrão é 16).
        usar_maiusculas (bool): Se deve incluir letras maiúsculas (padrão é True).
        usar_minusculas (bool): Se deve incluir letras minúsculas (padrão é True).
        usar_digitos (bool): Se deve incluir dígitos (padrão é True).
        usar_simbolos (bool): Se deve incluir símbolos (padrão é False).

    Retorna:
        str: Chave/senha secreta gerada.
    """
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos um conjunto de caracteres deve ser selecionado.")

    return ''.join(random.choice(caracteres) for _ in range(comprimento))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Gerar uma chave secreta/senha.")
    parser.add_argument("-c", "--comprimento", type=int, default=16, help="Comprimento da chave/senha (padrão é 16).")
    parser.add_argument("-m", "--usar_maiusculas", action="store_true", help="Incluir letras maiúsculas.")
    parser.add_argument("-n", "--usar_minusculas", action="store_true", help="Incluir letras minúsculas.")
    parser.add_argument("-d", "--usar_digitos", action="store_true", help="Incluir dígitos.")
    parser.add_argument("-s", "--usar_simbolos", action="store_true", help="Incluir símbolos.")

    args = parser.parse_args()

    try:
        chave_secreta = gerar_chave_secreta(
            comprimento=args.comprimento,
            usar_maiusculas=args.usar_maiusculas,
            usar_minusculas=args.usar_minusculas,
            usar_digitos=args.usar_digitos,
            usar_simbolos=args.usar_simbolos
        )
        print("Chave/Senha Secreta Gerada:", chave_secreta)
    except ValueError as ve:
        print("Erro:", ve)
