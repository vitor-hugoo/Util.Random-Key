# util.random.key
 Script para gerar uma chave aleatória

Para rodar o script:
python <nome_do_arquivo>.py parâmetros conforme exemplos

python generate_secret_key.py -l 20 -u -w -d

generate_secret_key:
    "-l", "--length",
    "-u", "--use_uppercase",
    "-w", "--use_lowercase",
    "-d", "--use_digits",
    "-s", "--use_symbols",


python gerar_chave_secreta.py -c 20 -m -n -d -s

gerar_chave_secreta:
    "-c", "--comprimento",
    "-m", "--usar_maiusculas",
    "-n", "--usar_minusculas",
    "-d", "--usar_digitos",
    "-s", "--usar_simbolos",
