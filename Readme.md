![icons8-python-150](https://github.com/KeilianeRocha/AlgoritmosComPython-/assets/109313933/d0bb8ba0-13e8-476e-8e0c-d9f29bedcdf4)

<h1 align="center"> Algoritmo Com Python </h1>
<p align="right">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO"/>
</p>

 # Resumo
>"Um algoritmo é uma sequência de raciocínios, instruções ou operações para alcançar um objetivo, sendo necessário que os passos sejam finitos e operados sistematicamente. Um algoritmo, portanto, conta com a entrada `(input)` e saída `(output)` de informações mediadas pelas instruções." [rockcontent](https://rockcontent.com/br/blog/algoritmo/#:~:text=Um%20algoritmo%20%C3%A9%20uma%20sequ%C3%AAncia,matem%C3%A1tico%20%C3%A1rabe%20do%20s%C3%A9culo%20IX.)

> As linguagens são como interpretes
- O Python é uma línguagem de propósito geral, podendo ser utilizada para *n* posibilidades
- Ela fácil e intuitiva
- É multiplataforma
- Baterry Included
- É livre
- Organizada
- Orientada a objetos
- Possui muitas bibliotecas

## Onde aplicar?

- Inteligência Artificial
- Biotecnologia
- Computação 3D

## Intalação

- O sistema operacional Windows não vem o o Python instalado
  
🔗 [Welcome to Python.org](https://www.python.org/)

⇒ Marcar “Add Path” 

⇒ Após instalado, devem aparecer os seguintes itens

>⇒ IDLE pode ser usado como o terminal

>- IDLE ⇒ É a função interativa, use para testar algo

>- Script ⇒ Use para programar

## Funções

```python
#print => imprima algo
print('Olá, Mundo!')

#input => Leia algo
nome = input('Qual o seu nome? ')
print(nome)
```

## Teoria

>**- Delimitadores ⇒ ' ' simples ou “ ” duplas para `Str`**
>   - Dentro das ‘ ’ ou “ ” Pode escrever em caixa alta
> 
>**- Variáveis ⇒ Espaço em memória que recebe algo**
> 
>    - Toda variável é um objeto, mas nem todo objeto é uma variável
>
>   - Quando menos variáveis vc utilizar, menos memória vc vai precisar
>    - Variável sempre em letra minúsculas
> 
>    - Variáveis sempre recebem algo por ⇒ =
>**- Comandos ⇒ Todo comando é uma função**
> 
>    - Toda função tem que ter ⇒ ()

**Sempre para `strings` => ' ' simples**
```python
print('olá, mundo!')
```
**A função `Input` sempre retorna uma `Str`**
```python
nome = input('Digite seu nome ')
```
**Se usar a função interna do operador, você perde a ordem de precedência**
```python
pow(4)
```
**O `print` é um `múdolo` interno do `Python`**
```python
print('nome')
```
**Alinhamento => {:>objeto} direita**
```python
nome = input('Digite seu nome: ')
print('Olá {:>20}'.format(nome))
```
**Alinhamento => {:<objeto} esquerda**
```python
nome = input('Digite seu nome: ')
print('Olá {:<20}'.format(nome))
```
*Alinhamento => {:^objeto} centralizado**
```python
nome = input('Digite seu nome: ')
print('Olá {:^20}'.format(nome))
```
**Alinhamento => {:=^objeto} centraliza => ===objeto===**
```python
nome = input('Digite seu nome: ')
print('Olá {:=^20}'.format(nome))
```
**Formatando números => {:n° de casasf} => 3.333333 => 3.333**
```python
n = float(input('um número'))
print('olá {:2f}'.format(n))
```
**Não quebrar linhas entre `prints` => ,end=' ') no final do primeiro `print`**
```python
n1 = float(input('Digite seu nome'))
n2 = float(input('Digite seu Sobrenome'))
print('olá {} {}'.format(n1,n2),end='')
```
**Quebrar linha dentro do ´print´,\n**
```python
n1 = float(input('Digite seu nome'))
n2 = float(input('Digite seu Sobrenome'))
print('olá {},\n{}'.format(n1,n2))
```
## Tipos primitivos

>1. int n° Inteiro (7, -4, 0, 9875)
>
>2. float => n° Real (4.5, 0.076, -15.223, 7.0) AK ponto flutuante ^^
>
>3. bool => (True, False) sempre com a primeira letra maiúscula
>
>4. str => ('olá', "olá", '7,5', '')
>

## Operações aritméticas

>+ => Adição
    5+2 == 7
>- => Subtração
    5-2 == 3
>* => Multiplicação (x ou .)
   5*2 == 10
>
>/ => Divisão
   5/2 == 2.5
>
>% => Módulo/ resto da divisão
   5%2 == 1
> 
>** => Potência
   5**2 == 25
> 
>// => Divisão inteira
   5//2 == 2

## Ordem de precedência

>1° => ()
> 
>2° => **
> 
>3° => *, /, //, %
> 
>4° => +, -

```python
nome = 'Test'
nome = "Test"
print(nome)
```


## Salvando ...

⇒ Crie uma pasta no computador

⇒ Abra a IDLE (utilizei o [PyCharm - Community](https://www.jetbrains.com/pycharm/download/other.html))

=> Crie um `diretório`

=> Dentro do diretório crie um `file.py`

⇒ Digite o Desafio 1

⇒ Salve o arquivo na pasta e
 execute => `run`


**EM CONSTRUÇÃO ...**

 
