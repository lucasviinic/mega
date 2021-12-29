# mega
Gerando jogos da Mega Sena utilizando números aleatórios verdadeiros

### Instalação e uso

1. Clone o repositório
2. Crie um ambiente virtual, ex `python -m venv .\virtualenv`
3. Com o ambiente ativo, instale as dependências com o comando `pip install -r requeriments.txt`
4. Rode o comando `python mega.py` e divirta-se (caso vá jogar, boa sorte!)

### A respeito dos números aleatórios

#### Pseudoaleatório

Você pode ter estranhado o uso do termo "aleatório verdadeiro", pois é comum pensar que os números aleatórios gerados por 
programas de computador sejam realmente aleatórios, mas não é bem assim. Há algoritmos por trás de tais implementações, entendendo
os passos do algoritmo, você pode prevê qual o número gerado em determinado momento, o que mostra que tais números aleatórios na verdade são bem previsíveis. Sendo assim,
os números aleatórios que conhecemos, como o fornecido pele método randint da biblioteca random do python, são na verdade _pseudoaleatórios_.

#### Aleatório verdadeiro

Para criar números aleatórios é interessante levar em consideração eventos que não estão no nosso controle, tendo isso em mente, o site
<a href="https://www.random.org/">random.org</a> gera números aleatórios com base no ruído atmosferico, garantindo assim a autenticidade
na aleatoriedade. Felizmente, a random possui uma API, e tal recurso está implementado na aplicação, gerendo todos os números de forma 
puramanete aleatória.

### Extra

Há um ótimo vídeo do Pedro Loss a respeito do porquê de computadores não poderem gerar números aleatórios, você pode conferir <a href="https://www.youtube.com/watch?v=LqXnpIn2Uxs">nesse link</a>.
