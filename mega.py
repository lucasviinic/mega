import requests

def get_random_number(quantity):
    response = requests.post('https://api.random.org/json-rpc/2/invoke', 
        json={
            "jsonrpc": "2.0",
            "method": "generateIntegerSequences",
            "params": {
                "apiKey": "ca3c0e5a-b78e-454a-999c-a1af4644ce6f",
                "n": quantity,
                "length": 6,
                "min": 1,
                "max": 60,
            "replacement": False,
                "base": 10
            },
            "id": 3076
    })

    jogos = response.json()['result']['random']['data']
    
    return jogos

def play(numero_de_jogos):
    jogos = get_random_number(numero_de_jogos)
    print('Aqui estão os seus jogos:')
    for jogo in jogos:
        print(f'Jogo Nº {jogos.index(jogo) + 1}: {jogo}')

    print('Boa sorte!! :)')

if __name__ == '__main__':
    while True:
        num = input('Quantos jogos você quer?: ')
        if num.isnumeric():
            num = int(num)
            if num > 0:
                play(num)
                res = input('Deseja jogar novamente? [S/N]: ')
                if res.upper() == 'N':
                    break
            else:
                print('Número inválido, o número deve ser maior do que 0')
        else:
            print('Caractere inválido, digite apenas números.')
